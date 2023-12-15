from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Fast API TUTORIAL",
              description="FastApi Tutorial by Andy",
              summary="Just a Tutorial",
              version="0.0.1",
              terms_of_service="https://example.com/terms/",
              contact={
                  "name": "Andy",
                  "email": "andy@example.com",
              },
              license_info={
                  "name": "Master license 101",
                  "url": "https://www.example.org/licenses/LICENSE-2.0.html",
              },
              )

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="The ID of the user you want to retrieve", gt=2),
        q: str = Query(None, max_length=5)
):
    return {"user": users[id], "query": q}


if __name__ == '__main__':
    pass
