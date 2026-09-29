"""Free local Hindi TTS interface.

Uses Edge TTS, which does not require a paid API key. The voice is configurable
so the same Hindi female voice can be used for every Prakriti video.
"""

import asyncio
from pathlib import Path

from config import OUTPUT_DIR

DEFAULT_VOICE = "hi-IN-SwaraNeural"


async def _save(text: str, output_path: str, voice: str) -> str:
    import edge_tts

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)
    return output_path


def generate_hindi_voice(
    text: str,
    output_path: str | None = None,
    voice: str = DEFAULT_VOICE,
) -> str:
    if not text or not text.strip():
        raise ValueError("TTS text is empty")

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    output = output_path or str(Path(OUTPUT_DIR) / "prakriti_voice.mp3")
    return asyncio.run(_save(text.strip(), output, voice))
