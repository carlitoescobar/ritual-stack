#!/bin/bash
echo "🔮 Initiating the Banishing Ritual..."

read -p "⚠️ This will remove the virtual environment, build directories, and local memory. Proceed? (y/N): " confirm

if [[ $confirm != "y" && $confirm != "Y" ]]; then
  echo "❌ Banishing ritual aborted. The Oracle remains."
  exit 1
fi

# Remove virtual environment
if [ -d "piper-venv" ]; then
  rm -rf piper-venv
  echo "💀 Virtual environment destroyed."
fi

# Remove memory
if [ -f "memory/memory_store.json" ]; then
  rm memory/memory_store.json
  echo "🧠 Memory layer exorcised."
fi

# Remove build artifacts
if [ -d "llama.cpp/build" ]; then
  rm -rf llama.cpp/build
  echo "🗿 Llama build purged."
fi

if [ -d "whisper.cpp/build" ]; then
  rm -rf whisper.cpp/build
  echo "📢 Whisper build purged."
fi

if [ -f "samples/ritual-stack-amy.wav" ]; then
  rm samples/ritual-stack-amy.wav
  echo "🔊 Sample voice output erased."
fi

echo "🚫 The Oracle has been banished... for now."
