# Install requirements
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "📦 Python dependencies imbibed."
else
  echo "⚠️ No requirements.txt found. Skipping spellbook install."
fi

# Set up memory layer
if [ ! -d "memory" ]; then
  mkdir memory
  echo "🧠 Carved memory chamber."
fi

if [ ! -f "memory/memory_store.json" ]; then
  echo "[]" > memory/memory_store.json
  echo "📂 Initialized Oracle's memory."
else
  echo "📁 Oracle's memory already exists."
fi

# Create directory structure if not already there
mkdir -p models samples scripts

# Optional: Auto-download Piper voice model or llama model (placeholder)
echo "👁️‍🗨️ Loading glyphs... (manual model download preferred for now)"

# Final incantation
echo "✨ Ritual complete. The Oracle awakens."
echo "Run with: source piper-venv/bin/activate"
