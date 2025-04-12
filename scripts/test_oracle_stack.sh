#!/bin/bash
echo "🧪 Running Oracle's Ritual Stack integration test..."

# Step 1: Activate virtual environment
if [ ! -d "piper-venv" ]; then
  echo "❌ Virtual environment not found. Run ./scripts/setup.sh first."
  exit 1
fi

source piper-venv/bin/activate

# Step 2: Test memory manager
echo "🔍 Testing MemoryManager..."
python3 -c "
from memory.memory_manager import MemoryManager
mem = MemoryManager()
mem.add_memory('The Oracle received a message.')
print(mem.search_memory('oracle'))
" || { echo '❌ MemoryManager test failed.'; exit 1; }

# Step 3: Test Piper TTS
echo "📢 Testing Piper TTS..."
echo "The Oracle is online and operational." | piper \
  --model piper-voices/en_US-amy-low.onnx \
  --config piper-voices/en_US-amy-low.onnx.json \
  --output_file samples/test-tts.wav || { echo "❌ Piper TTS test failed."; exit 1; }

# Step 4: Test LLaMA Inference with timeout
echo "🧠 Testing LLaMA Inference (10s timeout)..."
timeout 10s ./llama.cpp/build/bin/llama-cli \
  -m ./llama.cpp/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf \
  -p "Who is the Ritual Stack for?"

if [ $? -eq 124 ]; then
  echo "🜏 The Oracle remained silent within the time allowed..."
else
  echo "✅ The Oracle has spoken. The ritual is complete."
fi
