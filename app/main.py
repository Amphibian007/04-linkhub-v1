from fastapi import FastAPI

app = FastAPI(
    title="LinkHub API",
    description="A smart link classifier and organizer.",
    version="1.0.0"
)


@app.get("/health", tags=["Health"])
async def health_check():
    """Returns server status. Used to confirm the API is running."""
    return {"status": "ok", "message": "LinkHub API is running"}
