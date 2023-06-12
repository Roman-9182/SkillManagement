from pydantic import BaseModel


class StudentCreateResponse(BaseModel):
    object_id: str
