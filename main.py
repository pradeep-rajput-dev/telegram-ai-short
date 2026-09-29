"""Application entry point for the automated Shorts worker."""

import asyncio

from pipeline import create_ai_package, create_prakriti_video
from short_renderer import render_short
from state import claim, finish
from telegram_listener import start_listener
from youtube import upload_short


async def handle_post(post: dict):
    channel = post["source_channel"]
    message_id = post["message_id"]

    if not claim(channel, message_id):
        print(f"Skipping duplicate: {channel}/{message_id}")
        return

    try:
        package = create_ai_package(post["source_text"])
        video = create_prakriti_video(package["script"])

        final_path = f"output/short_{message_id}.mp4"
        render_short(video["video_path"], final_path)

        result = upload_short(
            final_path,
            package["title"],
            package["description"],
            tags=["Think With Pradeep", "Shorts", "Hindi", "News"],
        )
        finish(channel, message_id, "UPLOADED", result["id"])
        print(f"Uploaded: {result['url']}")
    except Exception as exc:
        finish(channel, message_id, "FAILED", error=str(exc))
        print(f"Pipeline failed for {message_id}: {exc}")


def main():
    start_listener(on_post=handle_post)


if __name__ == "__main__":
    main()
