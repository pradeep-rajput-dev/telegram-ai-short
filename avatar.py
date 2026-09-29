"""Free/open-source talking-head renderer interface for Prakriti.

This module keeps the presenter identity fixed. It expects a single master
reference image and a generated Hindi WAV file. A local Wav2Lip installation
can be connected through WAV2LIP_COMMAND.
"""

import os
import shlex
import subprocess
from pathlib import Path

from config import AVATAR_REFERENCE_IMAGE, OUTPUT_DIR


def render_prakriti(audio_path: str, output_path: str | None = None) -> str:
    reference = AVATAR_REFERENCE_IMAGE
    command = os.getenv("WAV2LIP_COMMAND", "").strip()

    if not reference:
        raise RuntimeError(
            "AVATAR_REFERENCE_IMAGE is not configured. Set it to Prakriti's "
            "master reference image. Do not generate a new face per video."
        )
    if not Path(reference).exists():
        raise FileNotFoundError(f"Prakriti reference image not found: {reference}")
    if not Path(audio_path).exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    if not command:
        raise RuntimeError(
            "WAV2LIP_COMMAND is not configured. Install/configure a local "
            "Wav2Lip-compatible renderer before running avatar generation."
        )

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    output = output_path or str(Path(OUTPUT_DIR) / "prakriti_avatar.mp4")

    cmd = shlex.split(command)
    cmd += ["--face", reference, "--audio", audio_path, "--outfile", output]

    # Wav2Lip preserves the supplied reference identity; it does not create a new face.
    # Outfit changes must use a selected reference image while keeping the same identity.
    subprocess.run(cmd, check=True)
    return output
