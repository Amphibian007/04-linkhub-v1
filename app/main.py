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
@app.get("/test-metadata", tags=["Health"])
async def test_metadata(url: str):
    """Temporary endpoint to test metadata fetching."""
    result = await fetch_metadata(url)
    return result



