import subprocess
import datetime
import json
import argparse

from memory_manager import MemoryManager  # Assumes it's in the same dir

MODEL_PATH = "models/mistral-7b-q4_k_m.gguf"
LLAMA_EXEC = "./llama.cpp/main"  # Path to llama.cpp compiled binary

def ask_llama(prompt):
    result = subprocess.run(
        [LLAMA_EXEC, "-m", MODEL_PATH, "-p", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def speak(text):
    subprocess.run(["python3", "scripts/say.py", text])  # Assuming say.py wraps Piper TTS

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
