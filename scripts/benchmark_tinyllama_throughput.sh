#!/bin/bash

echo "⚙️  Running throughput test (non-interactive, 64 tokens)..."

START=$(date +%s)

../llama.cpp/build/bin/llama-cli \
  -m ../llama.cpp/models/tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf \
  --prompt "Benchmarking throughput..." \
  --n-predict 64 \
  --ctx-size 512 \
  --batch-size 128 \
  --temp 0.7 \
  --top-p 0.9 \
  2>&1 | tee tmp_throughput.log

END=$(date +%s)
DURATION=$((END - START))

echo ""
TOKENS=$(grep 'tokens per second' tmp_throughput.log | tail -1 | awk '{print $(NF-3)}')
echo "🚀 Throughput: ${TOKENS:-unknown} tokens/sec"
echo "⏱️  Elapsed Time: ${DURATION}s"

rm tmp_throughput.log
echo "📈 Throughput test complete."
