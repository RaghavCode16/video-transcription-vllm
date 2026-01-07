import ffmpeg
from pathlib import Path


def extract_audio(video_path: str, output_path: str):
    """
    Extract audio from video and save as WAV.
    """
    video_path = Path(video_path)
    output_path = Path(output_path)

    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    (
        ffmpeg
        .input(str(video_path))
        .output(
            str(output_path),
            format="wav",
            acodec="pcm_s16le",
            ac=1,
            ar="16000"
        )
        .overwrite_output()
        .run(quiet=True)
    )

    return str(output_path)
