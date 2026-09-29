"""OpenAI-compatible AI client for script/title/description generation."""

import json
import requests

from config import AI_API_KEY, AI_MODEL
from prompts import SCRIPT_PROMPT, TITLE_PROMPT, DESCRIPTION_PROMPT
from config import CHANNEL_NAME

AI_BASE_URL = __import__("os").getenv(
    "AI_BASE_URL", "https://api.openai.com/v1"
).rstrip("/")


def _chat(prompt: str, temperature: float = 0.6) -> str:
    if not AI_API_KEY:
        raise RuntimeError("AI_API_KEY is not configured.")
    if not AI_MODEL:
        raise RuntimeError("AI_MODEL is not configured.")

    response = requests.post(
        f"{AI_BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {AI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": AI_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected AI response: {json.dumps(data)[:1000]}") from exc


def generate_script(source_text: str) -> str:
    return _chat(SCRIPT_PROMPT.format(text=source_text), temperature=0.5)


def generate_titles(script: str) -> list[str]:
    raw = _chat(TITLE_PROMPT.format(script=script), temperature=0.7)
    lines = [line.strip(" -•0123456789.)") for line in raw.splitlines() if line.strip()]
    return lines[:3]


def generate_description(script: str) -> str:
    return _chat(
        DESCRIPTION_PROMPT.format(script=script, channel_name=CHANNEL_NAME),
        temperature=0.5,
    )
