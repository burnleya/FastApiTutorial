from fastapi import FastAPI
from api import users, sections, courses

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

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


if __name__ == '__main__':
    pass
