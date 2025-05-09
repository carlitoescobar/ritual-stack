import os
import json
import requests
from memory_manager import MemoryManager

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "dolphin3-raw"
memory = MemoryManager("memory/oracle_memory.json")

def is_ollama_running():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=1)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False

def query_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    }
    with requests.post(f"{OLLAMA_URL}/api/generate", json=payload, stream=True) as r:
        response = ""
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                response += data.get("response", "")
        return response

def fallback_llama_cli(prompt):
    cmd = f"""llama.cpp/build/bin/llama-cli \\
      -m llama.cpp/models/tinystories-33m.Q2_K.gguf \\
      -p "{prompt}" \\
      --n-predict 128 --temp 0.7 --threads 12 --mlock"""
    return os.popen(cmd).read()

def interact():
    print("🔮 The Oracle is listening...\n")
    while True:
        user_input = input("🗣️ You: ").strip()
        if user_input.lower() in ("exit", "banish", "quit"):
            print("🛑 Banishing ritual complete.")
            break

        memory.save_interaction("user", user_input)

        if is_ollama_running():
            response = query_ollama(user_input)
        else:
            response = fallback_llama_cli(user_input)

        memory.save_interaction("oracle", response)
        print(f"🧠 Oracle: {response.strip()}\n")

if __name__ == "__main__":
    interact()
