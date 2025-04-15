from llama_cpp import Llama

llm = Llama(model_path="models/mistral-7b-q4_k_m.gguf", n_ctx=2048, chat_format="mistral-instruct")

response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of Texas?"}
    ],
    max_tokens=128,
    temperature=0.7,
)

print(response["choices"][0]["message"]["content"])
