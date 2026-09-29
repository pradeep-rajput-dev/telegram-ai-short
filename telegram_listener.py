"""Telegram source-channel listener.

Reads new text posts from the configured source channel using a Pyrogram
user session. The session string stays in an environment variable.
"""

from pyrogram import Client, filters
from pyrogram.types import Message

from config import (
    TELEGRAM_API_HASH,
    TELEGRAM_API_ID,
    TELEGRAM_SESSION_STRING,
    TELEGRAM_SOURCE_CHANNEL,
)
from pipeline import process_text


def build_client() -> Client:
    missing = [
        name
        for name, value in {
            "TELEGRAM_API_ID": str(TELEGRAM_API_ID),
            "TELEGRAM_API_HASH": TELEGRAM_API_HASH,
            "TELEGRAM_SESSION_STRING": TELEGRAM_SESSION_STRING,
            "TELEGRAM_SOURCE_CHANNEL": TELEGRAM_SOURCE_CHANNEL,
        }.items()
        if not value or value == "0"
    ]
    if missing:
        raise RuntimeError("Missing Telegram environment variables: " + ", ".join(missing))

    return Client(
        "think-with-pradeep-worker",
        api_id=TELEGRAM_API_ID,
        api_hash=TELEGRAM_API_HASH,
        session_string=TELEGRAM_SESSION_STRING,
    )


def start_listener(on_post=None):
    """Start the worker and call on_post(processed_post) for each text post."""
    app = build_client()

    @app.on_message(filters.chat(TELEGRAM_SOURCE_CHANNEL) & filters.text)
    async def handle_message(_, message: Message):
        try:
            processed = process_text(message.text or message.caption or "")
            processed["message_id"] = message.id
            processed["source_channel"] = TELEGRAM_SOURCE_CHANNEL
            if on_post:
                await on_post(processed)
            else:
                print(f"New Telegram post: {message.id}")
        except Exception as exc:
            print(f"Telegram post processing failed ({message.id}): {exc}")

    print(f"Listening to Telegram channel: {TELEGRAM_SOURCE_CHANNEL}")
    app.run()
