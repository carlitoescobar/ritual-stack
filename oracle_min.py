from llama_cpp import Llama

MODEL_PATH = "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=12,
    n_batch=64,
    chat_format=None,  # Raw prompt mode
    verbose=True
)

while True:
    try:
        prompt = input("\n> ").strip()
        if prompt.lower() in ["exit", "quit"]:
            print("🛑 Exiting Oracle.")
            break

        result = llm(prompt=prompt, max_tokens=128, temperature=1.0)
        response = result.get("choices", [{}])[0].get("text", "").strip()

        print(f"\nOracle: {response}")

    except KeyboardInterrupt:
        print("\n⚡ Oracle silenced.")
        break
