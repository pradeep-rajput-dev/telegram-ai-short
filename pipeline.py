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


def create_ai_package(text: str) -> dict:
    """Generate the spoken script and YouTube metadata from source text."""
    from ai_client import generate_description, generate_script, generate_titles

    script = generate_script(text)
    titles = generate_titles(script)
    description = generate_description(script)

    return {
        "source_text": text.strip(),
        "script": script,
        "titles": titles,
        "title": titles[0] if titles else "Think With Pradeep",
        "description": description,
        "status": "SCRIPT_READY",
    }
