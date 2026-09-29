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

CHANNEL_NAME = env("CHANNEL_NAME", "Think With Pradeep")
CHANNEL_USERNAME = env("CHANNEL_USERNAME", "thinkwithpradeep")
PRESENTER_NAME = env("PRESENTER_NAME", "Prakriti")
VOICE_NAME = env("VOICE_NAME", "hi-IN-SwaraNeural")
AVATAR_REFERENCE_IMAGE = env("AVATAR_REFERENCE_IMAGE")
OUTPUT_DIR = env("OUTPUT_DIR", "output")

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

YOUTUBE_CLIENT_ID = env("YOUTUBE_CLIENT_ID")
YOUTUBE_CLIENT_SECRET = env("YOUTUBE_CLIENT_SECRET")
YOUTUBE_REFRESH_TOKEN = env("YOUTUBE_REFRESH_TOKEN")

AI_BASE_URL = env("AI_BASE_URL", "https://api.openai.com/v1")
