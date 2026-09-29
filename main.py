"""Application entry point for the Telegram -> YouTube Shorts worker."""

from config import CHANNEL_NAME, PRESENTER_NAME
from telegram_listener import start_listener


async def handle_post(post: dict):
    # The next pipeline stages will turn this processed Telegram post into
    # script -> voice/avatar -> render -> YouTube upload.
    print(
        f"Received post {post.get('message_id')} | "
        f"presenter={PRESENTER_NAME} | channel={CHANNEL_NAME}"
    )


def main():
    start_listener(on_post=handle_post)


if __name__ == "__main__":
    main()
