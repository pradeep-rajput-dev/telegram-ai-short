# 🎬 Telegram AI Shorts

> **Telegram → AI → Prakriti → Premium Short → YouTube**

An automated YouTube Shorts generation system that reads text posts from your own Telegram channel, converts them into polished Hindi short-video scripts, presents them through a consistent AI news presenter named **Prakriti**, renders a premium 9:16 video, and uploads it to YouTube.

## ✨ Core Workflow

```
Telegram Channel
      ↓
New Text Post
      ↓
Duplicate Check
      ↓
AI Script Generation
      ↓
Prakriti AI Presenter
      ↓
Hindi Female News-Anchor Voice
      ↓
Lip Sync + Expressions
      ↓
Premium Visuals + Captions
      ↓
1080 × 1920 Short
      ↓
Title + Description + Hashtags
      ↓
YouTube Shorts Upload
```

## 👩 Prakriti: AI Presenter

**Prakriti** is the fixed virtual presenter identity of the project.

### Visual direction
- Adult Indian female presenter
- Attractive, polished and professional appearance
- Friendly but confident expression
- Premium newsroom/studio presentation
- Consistent face and overall appearance
- Natural facial expressions
- Subtle, realistic hand/body movement
- Modern professional outfit
- Clean premium background
- No exaggerated or cartoon-like presentation

### Voice direction
- Natural Hindi female voice
- Clear Hindi pronunciation
- News-anchor presentation style
- Confident and warm delivery
- Moderate speaking speed
- Human-like pauses and emphasis
- No robotic-sounding narration

The system should keep Prakriti visually and vocally consistent across generated Shorts.

## 🎨 Premium Video Design

Every Short should be designed for vertical mobile viewing:

- Resolution: **1080 × 1920**
- Aspect ratio: **9:16**
- Clean premium typography
- Animated subtitles
- Important words highlighted
- Smooth transitions
- News-style information cards
- Relevant background footage/images where appropriate
- Channel branding
- Prakriti presenter as the primary on-screen host
- Professional intro/outro kept short
- No unnecessary visual clutter

## 🏷️ Channel Branding

The channel name must appear in every generated Short.

Default:

**Think With Pradeep**

YouTube handle: **@thinkwithpradeep**

The channel name must be configurable through environment variables so it can be changed without editing source code.

Optional branding elements:
- Channel logo
- Watermark
- Social handle
- Small presenter identifier: **Prakriti**

## 🤖 AI Script Generation

The source Telegram text is treated as the information source.

The AI should:

1. Understand the source text.
2. Preserve factual information.
3. Create a natural Hindi spoken script.
4. Start with an engaging hook.
5. Keep the script suitable for approximately 30–60 seconds.
6. Avoid unnecessary filler.
7. Never invent facts, numbers, names or quotes.
8. Generate a YouTube-friendly title.
9. Generate a short description and relevant hashtags.

The original source should remain the factual basis of the Short.

## 📲 Telegram Input

The system will monitor a configured Telegram channel.

When a new eligible text post arrives:

- Extract the text.
- Identify the Telegram message ID.
- Check whether it was already processed.
- Generate the Short.
- Store processing status.
- Upload the finished video.

Duplicate Telegram messages must not create duplicate Shorts.

## ▶️ YouTube Upload

The system will support YouTube OAuth and upload generated videos automatically.

Upload metadata:

- Title
- Description
- Hashtags
- Shorts-friendly format
- Visibility setting
- Optional scheduled publishing

YouTube credentials and tokens must **never** be committed to GitHub.

## 🗂️ Project Structure

Planned structure:

```
telegram-ai-short/
├── main.py
├── config.py
├── telegram_client.py
├── ai_script.py
├── presenter.py
├── voice.py
├── subtitles.py
├── video_renderer.py
├── youtube.py
├── database.py
├── prompts.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── assets/
│   ├── presenter/
│   ├── backgrounds/
│   ├── music/
│   ├── fonts/
│   └── branding/
└── output/
```

## 🔐 Environment Configuration

Sensitive credentials belong in `.env` or the hosting provider's secret/environment-variable system.

Example configuration:

```env
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_SESSION_STRING=
TELEGRAM_SOURCE_CHANNEL=

AI_API_KEY=
AI_MODEL=

YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_REFRESH_TOKEN=

CHANNEL_NAME=INFO BYTES
PRESENTER_NAME=Prakriti

VOICE_LANGUAGE=hi-IN

VIDEO_WIDTH=1080
VIDEO_HEIGHT=1920
MAX_DURATION=60
```

## 🧠 Processing States

Each Telegram message should have a tracked state:

```
NEW
↓
PROCESSING
↓
SCRIPT_READY
↓
VIDEO_RENDERED
↓
UPLOADED
```

If an error occurs:

```
FAILED
```

The system should support safe retries without producing duplicate YouTube uploads.

## 🛡️ Reliability

The production version should include:

- Duplicate detection
- Retry handling
- Temporary-file cleanup
- Structured logs
- API error handling
- YouTube upload retry
- Telegram reconnect handling
- Database-backed processing state
- Configurable upload delay/schedule

## 🚀 Deployment

The project is intended to be deployable using Docker on services such as:

- Koyeb
- Render
- VPS
- AWS

FFmpeg must be available in the runtime environment.

## ⚠️ Content Responsibility

The Telegram source channel for this project is owned/controlled by the project owner. The automation is designed to transform the owner's source text into original video presentation.

AI-generated scripts should preserve the source facts and avoid fabricating information.

---

### Project Identity

**Presenter:** Prakriti  
**Format:** YouTube Shorts  
**Language:** Hindi  
**Style:** Premium AI News Presenter  
**Channel Name:** Think With Pradeep  
**YouTube Username:** @thinkwithpradeep
