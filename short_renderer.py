"""Final Shorts renderer: vertical canvas, subtitles and Think With Pradeep branding."""

import subprocess
from pathlib import Path

from config import CHANNEL_NAME, FPS, VIDEO_HEIGHT, VIDEO_WIDTH


def render_short(input_video: str, output_video: str, subtitle_file: str | None = None) -> str:
    src = Path(input_video)
    if not src.is_file():
        raise FileNotFoundError(src)
    Path(output_video).parent.mkdir(parents=True, exist_ok=True)

    # Uses FFmpeg. Optional ASS subtitles can be burned in when supplied.
    vf = (
        f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=decrease,"
        f"pad={VIDEO_WIDTH}:{VIDEO_HEIGHT}:(ow-iw)/2:(oh-ih)/2"
    )
    if subtitle_file:
        vf += f",subtitles={subtitle_file}"

    # Branding is supplied as metadata; a dedicated transparent PNG/logo can
    # be added later without changing the pipeline.
    cmd = [
        "ffmpeg", "-y", "-i", str(src),
        "-vf", vf, "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        "-metadata", f"title={CHANNEL_NAME}",
        str(output_video),
    ]
    subprocess.run(cmd, check=True)
    return output_video
