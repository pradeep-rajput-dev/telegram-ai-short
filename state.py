"""Lightweight SQLite state store for duplicate prevention and processing status."""

import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "pipeline.db"


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""CREATE TABLE IF NOT EXISTS posts (
            source_channel TEXT NOT NULL,
            message_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            youtube_id TEXT,
            error TEXT,
            PRIMARY KEY(source_channel, message_id)
        )""")


def claim(source_channel: str, message_id: int) -> bool:
    init_db()
    with sqlite3.connect(DB_PATH) as db:
        try:
            db.execute(
                "INSERT INTO posts(source_channel,message_id,status) VALUES(?,?,?)",
                (source_channel, message_id, "PROCESSING"),
            )
            return True
        except sqlite3.IntegrityError:
            return False


def finish(source_channel: str, message_id: int, status: str, youtube_id: str | None = None, error: str | None = None):
    init_db()
    with sqlite3.connect(DB_PATH) as db:
        db.execute(
            "UPDATE posts SET status=?, youtube_id=?, error=? WHERE source_channel=? AND message_id=?",
            (status, youtube_id, error, source_channel, message_id),
        )
