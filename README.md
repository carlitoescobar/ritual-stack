# Updated Oracle Stack

This project has been updated to move away from the base llama.cpp application. Instead, we now use a quantized Dolphin Llama 3 model that is uncensored and unbiased, integrated with Ollama and AnythingLLM as the base for Oracle.

## Overview

- **Dolphin Llama 3**: A quantized, uncensored, and unbiased model. The uncensored version allows for unrestricted content generation.
- **Ollama**: Used for model serving and inference.
- **AnythingLLM**: Provides additional capabilities and integration.

## Installation

Please refer to the updated installation instructions in the `scripts/` directory.

## Usage

Detailed usage instructions will be provided in the documentation.

---

## 🧙 The Oracle [0racle-01]
> A self-contained, cyberpunk-inspired intelligence node for the prepared technomancer. Built from bare metal. Fueled by silence. Whispering secrets in synthetic tongues.

---

## 📜 Lore

**The Oracle** is the central pillar of Oracle's Ritual Stack — a vertical cyberdeck designed to serve as a local AI librarian, assistant, and archivist. Forged with minimal dependencies, hardened for offline operation, and empowered by LLMs, voice synthesis, transcription, and memory.  

- ⚡ Built around the [Beelink SER5 Pro Mini PC](https://www.bee-link.com/)
- 🧠 Runs `llama.cpp`, `whisper.cpp`, and `piper` locally
- 🎙️ Features voice input/output (Whisper + Piper)
- 🧾 Persists memory in JSON (training-ready later)
- 🖥️ Displays on a 7.9" Waveshare vertical panel
- 🧩 Modular snap-fit 3D-printed monolith chassis (A1 Mini compatible)

---

## 🔧 Ritual Stack Components

| Component            | Role                         | Status       |
|----------------------|------------------------------|--------------|
| `llama.cpp`          | Local LLM (Mistral 7B)        | ✅ Installed |
| `whisper.cpp`        | Local Speech-to-Text          | ✅ Installed |
| `piper`              | Local Text-to-Speech          | ✅ Installed |
| `memory_manager.py`  | Persistent JSON Memory        | ✅ Installed |
| `oracle.py`          | Ritual core (TBD)             | 🚧 Planning  |
| `scripts/setup.sh`   | Full setup incantation        | ✅ Complete  |

---

## 🧰 Installation

```bash
git clone --recurse-submodules git@github.com:carlitoescobar/ritual-stack.git
cd ritual-stack
chmod +x scripts/setup.sh
./scripts/setup.sh
```

⚠️ Use `--recurse-submodules` to pull `llama.cpp`, `whisper.cpp`, and `piper`.

---

## 🧪 Usage

Basic memory test:

```bash
source piper-venv/bin/activate
python3 test_memory.py
```

Example entrypoint (coming soon):

```bash
python3 oracle.py
# > Oracle: "The Ritual Stack is online and operational."
```

---

## 🧼 Banishing Ritual

To teardown the stack and erase the Oracle's presence:

```bash
chmod +x scripts/banish.sh
./scripts/banish.sh
```

> *"All knowledge fades... until summoned again."*

---

## 🧩 Hardware

**Chassis**: 3D-printable monolith, modular, designed for A1 Mini  
**Display**: Waveshare 7.9" Vertical HDMI  
**Core**: Beelink SER5 Pro (Ryzen 5, 32GB RAM, 500GB NVMe)

STL files and build diagrams coming soon.

---

## 🧠 Future Expansions

- [ ] 🧮 Vector memory database integration (e.g. `faiss`, `chromadb`)
- [ ] 🛜 API gateway for remote endpoints (weather, news, data)
- [ ] 🔁 Fine-tuning + local retraining
- [ ] 🧵 Conversational chat UI (local or terminal)
- [ ] 📡 LoRa Mesh input/output (via TDeck)
- [ ] 🖼️ Embedded system dashboard for screen
- [ ] 📚 **Internet-in-a-Box node integration** (IIAB for offline content libraries, community mesh drops, and local educational resources)

> _"The Oracle shall one day speak not just with memory and voice, but with an entire shadow library encoded in her bones."_

---

## 🪪 Credits

- Voice: [`en_US-amy-low`](https://huggingface.co/rhasspy/piper-voices)
- Model: [`Mistral 7B v0.2 Q4_K_M`](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
- Tools: `llama.cpp`, `piper`, `whisper.cpp`, `Python`, `CMake`

---

## 🛑 Disclaimer

This stack is designed to function **entirely offline**. It does not call home, rely on external APIs, or leak data. Any remote integrations are opt-in.

**Use responsibly. Summon at your own risk.**
