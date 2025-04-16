import datetime
import json
import argparse
import subprocess
from memory.memory_manager import MemoryManager

MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

def ask_llama(prompt):
    print("[DEBUG] Invoking llama-cli subprocess...")
    try:
        process = subprocess.Popen(
            [
                "./llama.cpp/build/bin/llama-cli",
                "--no-warmup",
                "--log-disable",
                "--threads", "12",
                "--n-predict", "64",
                "--ctx-size", "2048",
                "--batch-size", "512",
                "-m", MODEL_PATH,
                "-p", prompt.strip(),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        try:
            stdout, stderr = process.communicate(timeout=60)
        except subprocess.TimeoutExpired:
            process.kill()
            return "[ERROR] Timeout waiting for model response."

        output = stdout + "\n" + stderr
        print("[DEBUG] Raw output:\n", output)

        # Attempt to extract response following prompt line
        lines = output.splitlines()
        for i, line in enumerate(lines):
            if prompt.strip() in line:
                response = "\n".join(lines[i + 1:]).strip()
                break
        else:
            response = output.strip()

        return response or "[Oracle returned no response]"

    except Exception as e:
        return f"[ERROR] Exception occurred: {str(e)}"

def speak(text):
    subprocess.run(["python3", "scripts/say.py", text])

def remember(memory, prompt, response):
    memory.save_entry(
        content=f"Q: {prompt}\nA: {response}",
        metadata={"source": "oracle.py"}
    )

def log_to_file(prompt, response, log_file):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}]\nQ: {prompt}\nA: {response}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Oracle CLI")
    parser.add_argument("--silent", action="store_true", help="Disable TTS")
    parser.add_argument("--memory-off", action="store_true", help="Disable memory logging")
    parser.add_argument("--voice", action="store_true", help="Enable Whisper voice input")
    args = parser.parse_args()

    memory = None if args.memory_off else MemoryManager("memory/memories.json")
    log_file = f"oracle_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    print("\U0001F52E Oracle is ready. Ask your question.")

    while True:
        try:
            if args.voice:
                user_input = subprocess.check_output(["python3", "scripts/listen.py"]).decode().strip()
                print(f"You said: {user_input}")
            else:
                user_input = input("\n> ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("\U0001F44B Farewell.")
                break

            response = ask_llama(user_input)
            print(f"\nOracle: {response}")

            if not args.silent:
                speak(response)

            if memory:
                remember(memory, user_input, response)

            log_to_file(user_input, response, log_file)

        except KeyboardInterrupt:
            print("\n\u26A1 Oracle silenced.")
            break

if __name__ == "__main__":
    main()
