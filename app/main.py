from fastapi import FastAPI
from app.services.supabase import supabase
from app.services.metadata import fetch_metadata

app = FastAPI(
    title="LinkHub API",
    description="A smart link classifier and organizer.",
    version="1.0.0"
)


@app.get("/health", tags=["Health"])
async def health_check():
    """Returns server status. Used to confirm the API is running."""
    return {"status": "ok", "message": "LinkHub API is running"}

from app.services.gemini import generate_ai_content

@app.get("/test-gemini", tags=["Health"])
async def test_gemini():
    """Temporary test endpoint for Gemini AI service."""
    result = await generate_ai_content(
        title="Async Python Tutorial for Beginners",
        description="Learn how to use async and await in Python with real examples.",
        platform="youtube"
    )
    return result

