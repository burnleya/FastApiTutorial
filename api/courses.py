from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()
courses = []


class Course(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/courses")
async def read_course():
    return {"courses": []}


@router.post("/courses")
async def create_course_api():
    return {"courses": []}


@router.get("/courses/{id}")
async def read_course(id: int):
    return {"courses": courses[id]}


@router.patch("/courses/:{id}")
async def update_course(id: int):
    return {"courses": courses[id]}


@router.delete("/courses/:{id}")
async def delete_course(id: int):
    return {"courses": courses[id]}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
