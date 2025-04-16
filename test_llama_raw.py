from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=12,
    chat_format=None,  # <-- important
    verbose=True
)

prompt = "What is the capital of France?"

output = llm(
    prompt,
    max_tokens=64,
    temperature=0.7,
    stop=["</s>"]  # explicitly define stop token
)

print("=== OUTPUT ===")
print(output.get("choices")[0].get("text", "").strip())
