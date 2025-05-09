#!/bin/bash

echo "🧙 Benchmarking TinyLlama on Oracle's Ritual Stack..."
MODEL_PATH="../llama.cpp/models/tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf"

# Set strict mode
set -e

time ../llama.cpp/build/bin/llama-cli \
  -m "$MODEL_PATH" \
  -i \
  --no-warmup \
  --prompt "The Oracle awakens. Speak, spirit." \
  --n-predict 32 \
  --ctx-size 512 \
  --batch-size 128 \
  --temp 0.7 \
  --top-p 0.9

echo "🏁 Benchmark complete."
