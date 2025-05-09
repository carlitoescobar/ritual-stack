#!/bin/bash
set -e

echo "🔮 Summoning Oracle's Dependencies..."
# Keep sudo session alive throughout the script
sudo -v

# Install critical system packages silently
echo "🛠 Installing system libraries (graphviz, build essentials)..."
sudo apt-get update -y
sudo apt-get install -y graphviz libgraphviz-dev build-essential python3-dev pkg-config

echo "🧪 Activating the Python Virtual Environment..."
# Create venv only if it doesn't exist
if [ ! -d "piper-venv" ]; then
    python3 -m venv piper-venv
fi
source piper-venv/bin/activate

echo "📦 Installing Ritual Python packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✨ Oracle's Ritual Stack is fully summoned and operational."
