import uvicorn
from fastapi import FastAPI

from app.endpoints.rest.students import student_router

app = FastAPI()
app.include_router(student_router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
