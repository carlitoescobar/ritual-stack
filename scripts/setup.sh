#!/bin/bash
echo "🧙 Setting up Oracle's Ritual Stack..."

# Pull submodules
echo "🔗 Initializing Git submodules..."
git submodule update --init --recursive

# Create and activate virtual environment
if [ ! -d "piper-venv" ]; then
  python3 -m venv piper-venv
  echo "✅ Virtual environment created."
else
  echo "🔁 Virtual environment already exists."
fi

source piper-venv/bin/activate

# Install requirements
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "📦 Python dependencies installed."
else
  echo "⚠️ No requirements.txt found. Skipping Python package install."
fi

echo "✨ Ritual complete. The Oracle awakens."
