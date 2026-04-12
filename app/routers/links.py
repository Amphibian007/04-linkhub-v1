from fastapi import APIRouter
from app.models.link import PreviewRequest, PreviewResponse
from app.services.metadata import fetch_metadata
from app.services.gemini import generate_ai_content

router = APIRouter()


@router.post("/links/preview", response_model=PreviewResponse, tags=["Links"])
async def preview_link(request: PreviewRequest):
    """Fetches metadata and AI summary for a URL without saving it."""
    metadata = await fetch_metadata(request.url)

    ai_content = await generate_ai_content(
        title=metadata["title"],
        description=metadata["description"],
        platform=metadata["platform"]
    )

    return PreviewResponse(
        url=request.url,
        platform=metadata["platform"],
        title=metadata["title"],
        description=metadata["description"],
        thumbnail=metadata["thumbnail"],
        summary=ai_content["summary"],
        tags=ai_content["tags"]
    )
