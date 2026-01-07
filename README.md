# Video Call Transcription & Emotion Metadata System

## Overview

This project implements a simple, end-to-end pipeline that processes recorded video calls and produces timestamped transcriptions enriched with emotion and delivery metadata using a Large Language Model (LLM).

The system focuses on **audio and language signals** and is designed as a clean, modular MVP that can be extended in the future.

---

## What It Does

Given a recorded `.mp4` video call, the system:

1. Extracts audio from the video
2. Transcribes speech with timestamps
3. Analyzes each segment using an LLM to infer:
   - Emotion
   - Tone
   - Speaking pace
   - Conversational intent
4. Outputs both human-readable and structured results

---

## Architecture

```

Video (.mp4)
→ Audio Extraction (FFmpeg)
→ Speech-to-Text (Whisper)
→ LLM Metadata Analysis
→ Transcript Output (TXT + JSON)

```

Each stage is isolated and replaceable, enabling easy iteration and future expansion.

---

## Tech Stack

- Python
- FFmpeg (audio extraction)
- OpenAI Whisper (speech-to-text)
- OpenAI API (LLM analysis)
- Docker (optional, recommended)

---

## Project Structure

```

app/
├─ main.py
└─ pipeline/
├─ audio_extractor.py
├─ transcriber.py
└─ emotion_analyzer.py

data/
├─ input/
│  └─ sample_call.mp4
└─ output/
├─ transcript.txt
└─ enriched_transcription.json

```

---

## Setup

### Environment Variables

Create a `.env` file:

```

OPENAI_API_KEY=your_openai_api_key

```

---

## Running Locally

```bash
python -m app.main
```

Input video:

```
data/input/sample_call.mp4
```

---

## Docker (Recommended)

```bash
docker compose build
docker compose up
```

---

## Output

After execution, the following files are generated:

- `data/output/transcript.txt` – readable transcript with metadata
- `data/output/enriched_transcription.json` – structured output for programmatic use

---

## Notes

- Designed as a batch MVP (not real-time)
- Audio-only analysis for reliability and performance
- Clean architecture suitable for extension

---

## Future Scope

- Speaker diarization
- Visual emotion analysis
- Real-time streaming
- API deployment

```

