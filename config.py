import os
from dotenv import load_dotenv

load_dotenv()

def env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()

TELEGRAM_API_ID = int(env("TELEGRAM_API_ID", "0") or 0)
TELEGRAM_API_HASH = env("TELEGRAM_API_HASH")
TELEGRAM_SESSION_STRING = env("TELEGRAM_SESSION_STRING")
TELEGRAM_SOURCE_CHANNEL = env("TELEGRAM_SOURCE_CHANNEL")

AI_API_KEY = env("AI_API_KEY")
AI_MODEL = env("AI_MODEL")

CHANNEL_NAME = env("CHANNEL_NAME", "INFO BYTES")
PRESENTER_NAME = env("PRESENTER_NAME", "Prakriti")

VIDEO_WIDTH = int(env("VIDEO_WIDTH", "1080"))
VIDEO_HEIGHT = int(env("VIDEO_HEIGHT", "1920"))
MAX_DURATION = int(env("MAX_DURATION", "60"))
FPS = int(env("FPS", "30"))

TTS_PROVIDER = env("TTS_PROVIDER")
TTS_API_KEY = env("TTS_API_KEY")
AVATAR_PROVIDER = env("AVATAR_PROVIDER")
AVATAR_API_KEY = env("AVATAR_API_KEY")
AVATAR_ID = env("AVATAR_ID")

UPLOAD_PRIVACY = env("UPLOAD_PRIVACY", "private")
