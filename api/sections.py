from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()
sections = []


class Sections(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/sections", response_model=List[Sections])
async def read_section():
    return sections


@router.get("/sections/:id/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/{id}")
async def read_content_blocks():
    return {"courses": []}