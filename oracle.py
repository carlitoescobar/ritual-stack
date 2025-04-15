import datetime
import json
import argparse
from llama_cpp import Llama
from memory.memory_manager import MemoryManager

MODEL_PATH = "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=12, n_batch=64, verbose=True)

def ask_llama(prompt):
    print("[DEBUG] Sending prompt to model...")
    try:
        start = datetime.datetime.now()

        result = llm(
            prompt=prompt,
            max_tokens=128,
            temperature=0.7,
            stop=["</s>"]
        )

        print("[DEBUG] Raw result from model:")
        print(json.dumps(result, indent=2))

        response = result.get("choices", [{}])[0].get("text", "[Oracle returned no text response]").strip()
        duration = (datetime.datetime.now() - start).total_seconds()
        print(f"\n[DEBUG] Response received in {duration:.2f} seconds.")
        return response

    except Exception as e:
        print(f"[ERROR] Failed to get response from model: {e}")
        return "[Oracle failed to respond]"

def speak(text):
    import subprocess
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
                import subprocess
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
            print("\n⚡ Oracle silenced.")
            break

if __name__ == "__main__":
    main()
