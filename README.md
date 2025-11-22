# self-hosted-jarvis
This project showcases an ai driven, self hosted assistant that connects to my home IoT devices, holds conversations, and can run scripts.

# Home AI Assistant

A fully local, privacy‑focused voice assistant integrating **Home
Assistant**, **local LLMs**, **wake word detection**, **STT/TTS**, and
smart‑home control.

This project aims to create a fully offline alternative to cloud voice
assistants with full customizability, voice training, and deep
smart‑home integration.

------------------------------------------------------------------------

## 🚀 Features

### 🔊 Voice Interaction

-   Wake‑word detection (`openWakeWord`)
-   VAD (Silero)
-   Speech‑to‑text (Faster‑Whisper)
-   Local LLM reasoning (Ollama or llama.cpp)
-   Text‑to‑speech (Piper)
-   Optional custom voice training

### 🏠 Smart Home Integration

-   Home Assistant service calls\
-   Control lights, vacuums, media, sensors\
-   Query home state ("is the garage open?")\
-   Add routines and behaviors

### 🧠 Brain Architecture

-   Function‑calling LLM
-   Local tool execution
-   Semantic memory (Chroma / LanceDB)
-   Persona and long‑term memory
-   Speaker verification (SpeechBrain)

### 📺 Media & Device Integrations

-   Roku TV control (ECP)
-   Jellyfin search & playback
-   Spotify (optional)
-   Wake‑on‑LAN

------------------------------------------------------------------------

## 📂 Project Structure

    assistant/
      main.py
      ha_client.py
      stt.py
      tts.py
      llm.py
      wakeword.py
      vad.py
      config/
    models/
    docs/
    scripts/

------------------------------------------------------------------------

## 🔧 Requirements

-   Windows PC with GPU (AMD RX 7600 recommended)
-   Debian server running Home Assistant
-   Python 3.10+
-   Docker (for backend services)
-   WireGuard (optional remote use)

------------------------------------------------------------------------

## 📦 Installation

Full setup instructions are provided in the `docs/` directory.\
Users can clone and follow the step‑by‑step guide for:

-   Installing Ollama or llama.cpp\
-   Installing Piper\
-   Connecting to Home Assistant\
-   Running your first voice command

------------------------------------------------------------------------

## 📝 License

This project is released under the **MIT License**

------------------------------------------------------------------------

## 📹 Demo (coming soon)

A video demonstration will be added once the assistant reaches its first
full prototype stage.
