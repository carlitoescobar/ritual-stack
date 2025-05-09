#!/usr/bin/env python3
import subprocess

LLAMA_CLI = "../llama.cpp/build/bin/llama-cli"
MODEL_PATH = "../llama.cpp/models/tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf"

def ask_oracle(prompt):
    cmd = [
        LLAMA_CLI,
        "-m", MODEL_PATH,
        "--n-predict", "64",
        "--ctx-size", "256",
        "--batch-size", "64",
        "--temp", "0.7",
        "--top-p", "0.9",
        "-p", prompt
    ]

    print("🔮 ", end="", flush=True)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    seen_prompt = False
    try:
        for line in iter(process.stdout.readline, ''):
            if prompt.strip() in line:
                seen_prompt = True
                continue
            if seen_prompt:
                print(line.strip(), end=' ', flush=True)
    except KeyboardInterrupt:
        process.kill()
        print("\n🛑 Oracle interrupted.")
    finally:
        process.stdout.close()
        process.wait()

if __name__ == "__main__":
    try:
        question = input("💬 Ask the Oracle: ")
        ask_oracle(question)
    except KeyboardInterrupt:
        print("\n🛑 Session ended.")
