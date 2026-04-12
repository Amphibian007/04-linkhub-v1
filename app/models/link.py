from pydantic import BaseModel
from typing import Optional


class PreviewRequest(BaseModel):
    url: str


class PreviewResponse(BaseModel):
    url: str
    platform: str
    title: str
    description: str
    thumbnail: Optional[str]
    summary: str
    tags: list[str]
