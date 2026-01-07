import whisper


def transcribe_audio(audio_path: str):
    """
    Transcribes audio using OpenAI Whisper and returns timestamped segments.
    """
    model = whisper.load_model("small")

    result = model.transcribe(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": round(seg["start"], 2),
            "end": round(seg["end"], 2),
            "text": seg["text"].strip()
        })

    return segments
