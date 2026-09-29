"""YouTube Data API v3 uploader.

Uses an OAuth refresh token so the deployed worker can upload without
interactive Google login.
"""

from pathlib import Path
from typing import Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from config import (
    YOUTUBE_CLIENT_ID,
    YOUTUBE_CLIENT_SECRET,
    YOUTUBE_REFRESH_TOKEN,
    UPLOAD_PRIVACY,
)

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def _credentials() -> Credentials:
    missing = [
        name
        for name, value in {
            "YOUTUBE_CLIENT_ID": YOUTUBE_CLIENT_ID,
            "YOUTUBE_CLIENT_SECRET": YOUTUBE_CLIENT_SECRET,
            "YOUTUBE_REFRESH_TOKEN": YOUTUBE_REFRESH_TOKEN,
        }.items()
        if not value
    ]
    if missing:
        raise RuntimeError("Missing YouTube environment variables: " + ", ".join(missing))

    credentials = Credentials(
        token=None,
        refresh_token=YOUTUBE_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=YOUTUBE_CLIENT_ID,
        client_secret=YOUTUBE_CLIENT_SECRET,
        scopes=SCOPES,
    )
    credentials.refresh(Request())
    return credentials


def youtube_service():
    return build("youtube", "v3", credentials=_credentials(), cache_discovery=False)


def get_channel_info() -> dict:
    """Verify OAuth and return the authenticated YouTube channel."""
    response = youtube_service().channels().list(
        part="snippet,contentDetails",
        mine=True,
    ).execute()

    items = response.get("items", [])
    if not items:
        raise RuntimeError("No YouTube channel is available to this Google account.")

    item = items[0]
    return {
        "id": item["id"],
        "title": item["snippet"]["title"],
        "url": f"https://www.youtube.com/channel/{item['id']}",
    }


def upload_short(
    video_path: str,
    title: str,
    description: str = "",
    tags: Optional[list[str]] = None,
    category_id: str = "25",
) -> dict:
    """Upload one rendered Short and return its YouTube metadata.

    The video file must already be rendered as a vertical 9:16 MP4.
    """
    path = Path(video_path)
    if not path.is_file():
        raise FileNotFoundError(f"Video not found: {path}")

    body = {
        "snippet": {
            "title": title[:100],
            "description": description,
            "tags": (tags or [])[:500],
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": UPLOAD_PRIVACY,
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        str(path),
        mimetype="video/mp4",
        resumable=True,
        chunksize=8 * 1024 * 1024,
    )

    request = youtube_service().videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        _, response = request.next_chunk()

    video_id = response["id"]
    return {
        "id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "status": response.get("status", {}),
    }
