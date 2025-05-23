import datetime
import json
import argparse
import subprocess
import time
import sys
import requests
from memory.memory_manager import MemoryManager

def ask_ollama(prompt, max_tokens: int = 64, temperature: float = 1.0) -> str:
    """
    Send a prompt to the Ollama API and stream the response.
    Returns the full response text.
    """
    try:
        response = ""
        first_token = True
        # Prepare the request to the Ollama API
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "dolphin-llama3:8b-256k-v2.9-q2_K",
            "prompt": prompt.strip(),
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": True
        }
        # Send the request and stream the response
        with requests.post(url, json=data, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    json_response = json.loads(line)
                    token = json_response.get("response", "")
                    if token:
                        if first_token:
                            # Clear the spinner and print the first token
                            sys.stdout.write("\r" + " " * 50 + "\r")
                            first_token = False
                        print(token, end="", flush=True)
                        response += token
                    elif first_token:
                        # Show spinner only while waiting for first token
                        sys.stdout.write("\r" + " " * 50 + "\r")
                        sys.stdout.write("Thinking... " + "|/-\\"[int(time.time() * 4) % 4])
                        sys.stdout.flush()
        return response or "[Oracle returned no response]"
    except Exception as e:
        # Clear the spinner in case of error
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()
        return f"[ERROR] Exception occurred: {str(e)}"

def speak(text):
    subprocess.run(["python3", "scripts/say.py", text])

def main():
    parser = argparse.ArgumentParser(description="Oracle CLI")
    parser.add_argument("--silent", action="store_true", help="Disable TTS")
    parser.add_argument("--memory-off", action="store_true", help="Disable memory logging")
    parser.add_argument("--voice", action="store_true", help="Enable Whisper voice input")
    args = parser.parse_args()

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
            response = ask_ollama(user_input)
            # Ensure newline after streaming tokens
            print()

            if not args.silent:
                speak(response)

        except KeyboardInterrupt:
            print("\n\u26A1 Oracle silenced.")
            break

if __name__ == "__main__":
    main()
