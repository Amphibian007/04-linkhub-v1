import httpx
from bs4 import BeautifulSoup
import yt_dlp


def detect_platform(url: str) -> str:
    """Detects the platform from the URL string."""
    url = url.lower()
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    elif "facebook.com" in url:
        return "facebook"
    elif "github.com" in url:
        return "github"
    elif "drive.google.com" in url:
        return "drive"
    elif "docs.google.com/document" in url:
        return "docs"
    elif "docs.google.com/spreadsheets" in url:
        return "sheets"
    else:
        return "unknown"


async def fetch_generic_metadata(url: str) -> dict:
    """Fetches title and description from any webpage using httpx and BeautifulSoup."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else ""
        description = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta and meta.get("content"):
            description = meta["content"].strip()

        return {"title": title, "description": description}


async def fetch_youtube_metadata(url: str) -> dict:
    """Fetches title and thumbnail from a YouTube URL using yt-dlp."""
    opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title", ""),
            "thumbnail": info.get("thumbnail", "")
        }


async def fetch_metadata(url: str) -> dict:
    """Main entry point. Detects platform and fetches appropriate metadata."""
    platform = detect_platform(url)

    if platform == "youtube":
        data = await fetch_youtube_metadata(url)
        return {
            "platform": platform,
            "title": data["title"],
            "description": "",
            "thumbnail": data["thumbnail"]
        }
    else:
        data = await fetch_generic_metadata(url)
        return {
            "platform": platform,
            "title": data["title"],
            "description": data["description"],
            "thumbnail": ""
        }
