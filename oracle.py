import datetime
import json
import argparse
import subprocess
from memory.memory_manager import MemoryManager

MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
from llama_cpp import Llama

# Initialize Llama model for streaming
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=12,
    n_batch=512,
    verbose=False,
    chat_format="mistral-instruct"
)

def ask_llama(prompt, max_tokens: int = 64, temperature: float = 1.0) -> str:
    """
    Stream tokens from the Llama model for the given prompt.
    Returns the full response text.
    """
    try:
        response = ""
        # Begin streaming chat completion
        for event in llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.strip()}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
        ):
            # Extract token content
            token = event.get("choices", [{}])[0].get("delta", {}).get("content", "")
            if token:
                print(token, end="", flush=True)
                response += token
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

            # Stream and display Oracle response
            print("\nOracle: ", end="", flush=True)
            response = ask_llama(user_input)
            # Ensure newline after streaming tokens
            print()

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
