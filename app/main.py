from fastapi import FastAPI
from app.services.supabase import supabase

app = FastAPI(
    title="LinkHub API",
    description="A smart link classifier and organizer.",
    version="1.0.0"
)


@app.get("/health", tags=["Health"])
async def health_check():
    """Returns server status. Used to confirm the API is running."""
    return {"status": "ok", "message": "LinkHub API is running"}


@app.get("/test-db", tags=["Health"])
async def test_db():
    """Tests the Supabase connection by fetching rows from the links table."""
    response = supabase.table("links").select("*").execute()
    return {"status": "ok", "rows": response.data}
