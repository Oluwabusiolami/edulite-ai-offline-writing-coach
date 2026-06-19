#!/usr/bin/env bash
set -euo pipefail

echo "Preparing EduLite AI model folder..."

mkdir -p model

MODEL_PATH="model/qwen2.5-1.5b-instruct-q4_k_m.gguf"
MODEL_URL="https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf?download=true"

if [ -f "$MODEL_PATH" ]; then
  echo "Model already exists at $MODEL_PATH"
  exit 0
fi

echo "Downloading Qwen2.5-1.5B-Instruct Q4_K_M GGUF model..."
echo "This may take some time depending on internet speed."

if command -v wget >/dev/null 2>&1; then
  wget -O "$MODEL_PATH" "$MODEL_URL"
elif command -v curl >/dev/null 2>&1; then
  curl -L -o "$MODEL_PATH" "$MODEL_URL"
else
  echo "Error: Please install wget or curl to download the model."
  exit 1
fi

echo "Download complete."
echo "Model saved at: $MODEL_PATH"
