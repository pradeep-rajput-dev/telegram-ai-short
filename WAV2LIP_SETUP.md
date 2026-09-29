# Wav2Lip setup

The repository does not bundle model weights or a GPU runtime. Install Wav2Lip locally or on a GPU worker, then set:

WAV2LIP_COMMAND=<your Wav2Lip inference command>

The command must accept:
- --face <Prakriti reference image>
- --audio <generated Hindi audio>
- --outfile <output mp4>

Keep the same Prakriti reference image for identity consistency. Use only Western professional outfits in reference images.

## Test

1. Put the master Prakriti image at a local path.
2. Generate a short Hindi WAV/MP3 with tts.py.
3. Configure WAV2LIP_COMMAND.
4. Run avatar.render_prakriti().
5. Verify the resulting MP4 before enabling automatic publishing.

Do not commit model weights, API keys, session strings, OAuth secrets, or reference images containing private information to GitHub.
