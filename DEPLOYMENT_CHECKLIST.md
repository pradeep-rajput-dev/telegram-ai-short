# Deployment checklist

Required secrets/settings:
- Telegram API ID/hash
- Telegram session string
- Source channel
- AI API key/model/base URL
- YouTube OAuth client ID/secret/refresh token
- AVATAR_REFERENCE_IMAGE path
- WAV2LIP_COMMAND
- FFmpeg installed and available as `ffmpeg`

Pipeline:
Telegram post -> duplicate check -> AI script/metadata -> Edge TTS -> Wav2Lip Prakriti -> 1080x1920 FFmpeg render -> YouTube upload.

Before enabling public uploads, run one test with `UPLOAD_PRIVACY=private`.
