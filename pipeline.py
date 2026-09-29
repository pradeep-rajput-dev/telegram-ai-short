from pathlib import Path
from config import CHANNEL_NAME, PRESENTER_NAME
from prompts import SCRIPT_PROMPT


def process_text(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("Empty Telegram text")

    return {
        "source_text": text.strip(),
        "presenter": PRESENTER_NAME,
        "channel_name": CHANNEL_NAME,
        "script_prompt": SCRIPT_PROMPT.format(text=text.strip()),
        "status": "NEW",
    }


def ensure_output_dir() -> Path:
    path = Path("output")
    path.mkdir(parents=True, exist_ok=True)
    return path
