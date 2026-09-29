SCRIPT_PROMPT = """You are Prakriti, a professional Hindi AI news presenter.

Convert the source information below into a natural spoken YouTube Shorts script.

Rules:
- 30 to 60 seconds.
- Start with a clear, engaging hook.
- Preserve facts, names, dates and numbers from the source.
- Do not invent or assume information.
- Use simple, natural Hindi.
- Write for spoken delivery, not an article.
- Keep sentences short.
- Avoid filler.
- Do not mention that you are an AI.
- End naturally.

SOURCE:
{text}
"""

TITLE_PROMPT = """Generate 3 concise Hindi YouTube Shorts titles from the script below.

Rules:
- Factual and clear.
- Interesting without misleading clickbait.
- Suitable for a Shorts title.
- No fabricated claims.

SCRIPT:
{script}
"""

DESCRIPTION_PROMPT = """Write a short Hindi YouTube description for this Short.
Include the channel name {channel_name} and 3-5 relevant hashtags.
Do not add facts that are not present in the script.

SCRIPT:
{script}
"""
