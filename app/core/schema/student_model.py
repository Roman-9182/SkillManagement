from pydantic import BaseModel, Field


class StudentModel(BaseModel):
    fullname: str
    email: str
    course_of_study: str
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)


class CreateStudentModel(BaseModel):
    fullname: str
    email: str | None
    course_of_study: str | None
    year: int
    gpa: float | None
