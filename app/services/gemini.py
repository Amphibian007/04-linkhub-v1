import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


async def generate_ai_content(title: str, description: str, platform: str) -> dict:
    """Sends link metadata to Gemini and returns a summary and tag suggestions."""

    prompt = f"""
You are a link organizer assistant.

Given the following link metadata, return a JSON object with exactly two fields:
- "summary": a single sentence (max 20 words) describing what this link is about
- "tags": a list of 2 to 3 short lowercase tags relevant to this link

Metadata:
- Title: {title}
- Description: {description}
- Platform: {platform}

Reply with valid JSON only. No explanation. No markdown. Example format:
{{"summary": "A tutorial on building REST APIs with FastAPI.", "tags": ["python", "fastapi", "tutorial"]}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    text = response.text.strip()

    result = json.loads(text)
    return result
