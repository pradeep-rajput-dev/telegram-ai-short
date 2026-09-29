"""Application entry point.

The production pipeline is:
Telegram -> AI script -> Prakriti presenter -> render -> YouTube.

Provider-specific implementations are intentionally isolated so they can be
changed without rewriting the rest of the application.
"""

from config import CHANNEL_NAME, PRESENTER_NAME
from pipeline import process_text


def main():
    print(f"{CHANNEL_NAME} | Presenter: {PRESENTER_NAME}")
    print("Telegram AI Shorts pipeline is ready.")
    print("Connect the configured Telegram, AI, presenter and YouTube providers.")


if __name__ == "__main__":
    main()
