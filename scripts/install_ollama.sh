#!/bin/bash

# Updated install_ollama.sh script for Oracle Stack
# This script installs Ollama and sets up the quantized Dolphin Llama 3 model with AnythingLLM integration

echo "Starting Ollama installation and setup..."

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Verify Ollama installation
if ! command -v ollama &> /dev/null; then
    echo "Ollama installation failed. Please check the installation process."
    exit 1
fi

echo "Ollama installed successfully."

# Download quantized Dolphin Llama 3 model
echo "Downloading quantized Dolphin Llama 3 model..."
# Replace the URL with the actual download link for the quantized model
curl -L -o dolphin_llama3_quantized.gguf https://example.com/dolphin_llama3_quantized.gguf

# Verify model download
if [ ! -f dolphin_llama3_quantized.gguf ]; then
    echo "Failed to download the Dolphin Llama 3 model. Please check the download link."
    exit 1
fi

echo "Dolphin Llama 3 model downloaded successfully."

# Setup AnythingLLM integration
echo "Setting up AnythingLLM integration..."
# Add commands to configure AnythingLLM with Ollama and the Dolphin model
# Example: python setup_anythingllm.py --model dolphin_llama3_quantized.gguf

echo "Installation and setup completed successfully." 