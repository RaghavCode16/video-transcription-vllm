from app.pipeline.audio_extractor import extract_audio
from app.pipeline.transcriber import transcribe_audio
from app.pipeline.emotion_analyzer import analyze_segment
import json

VIDEO_PATH = "data/input/sample_call.mp4"
AUDIO_PATH = "data/output/audio.wav"

if __name__ == "__main__":
    # Step 1: Extract audio
    extract_audio(VIDEO_PATH, AUDIO_PATH)
    print("Audio extracted successfully:", AUDIO_PATH)

    # Step 2: Transcribe audio
    segments = transcribe_audio(AUDIO_PATH)

    enriched_output = []

    print("\nTranscription Output:\n")

    for seg in segments:
        raw_metadata = analyze_segment(seg["text"])

        if isinstance(raw_metadata, str):
            metadata = json.loads(raw_metadata)
        else:
            metadata = raw_metadata

        entry = {
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"],
            "metadata": metadata,
        }

        enriched_output.append(entry)

        print(f"[{seg['start']}s - {seg['end']}s] {seg['text']}")
        print(metadata)
        print("-" * 50)

    # Save enriched JSON
    with open("data/output/enriched_transcription.json", "w") as f:
        json.dump(enriched_output, f, indent=2)

    # Save human-readable transcript
    with open("data/output/transcript.txt", "w") as f:
        for entry in enriched_output:
            f.write(
                f"[{entry['start']}s - {entry['end']}s] {entry['text']}\n"
                f"Emotion: {entry['metadata']['emotion']}, "
                f"Tone: {entry['metadata']['tone']}, "
                f"Pace: {entry['metadata']['pace']}, "
                f"Reaction: {entry['metadata']['reaction']}\n\n"
            )
