from fastapi import FastAPI
from app.routers import links

app = FastAPI(
    title="LinkHub API",
    description="A smart link classifier and organizer.",
    version="1.0.0"
)

app.include_router(links.router)


@app.get("/health", tags=["Health"])
async def health_check():
    """Returns server status. Used to confirm the API is running."""
    return {"status": "ok", "message": "LinkHub API is running"}
