#!/bin/bash
# 🔮 Oracle Benchmark Ritual

echo "🔮 Oracle Benchmark Ritual Initiated..."

# Set the model path correctly (inside llama.cpp/models)
MODEL_PATH="../llama.cpp/models/tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf"
LLAMA_CLI="../llama.cpp/build/bin/llama-cli"

# 🧪 Quick latency test (1 prompt, 1 output)
echo "🧪 Testing response speed..."
time $LLAMA_CLI \
    -m "$MODEL_PATH" \
    -p "The Oracle awakens." \
    --n-predict 1 \
    --ctx-size 512 \
    --batch-size 128 \
    --temp 0.7 \
    --top-p 0.9 \
    > /dev/null

echo "⏳ Latency test complete."

# 📈 Throughput test (generate 64 tokens)
echo "📈 Testing raw throughput..."
time $LLAMA_CLI \
    -m "$MODEL_PATH" \
    -p "The Oracle awakens." \
    --n-predict 64 \
    --ctx-size 512 \
    --batch-size 128 \
    --temp 0.7 \
    --top-p 0.9 \
    > /dev/null

echo "🏁 Oracle Benchmark Ritual Complete."
