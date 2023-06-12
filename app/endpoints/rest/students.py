from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from app.managers.mongo.student_manager import StudentManager
from app.core.db_connections.mongo_db import database
from app.core.schema.student_model import StudentModel
from app.core.schema.response_model import StudentCreateResponse
student_router = APIRouter(tags=["student_router"])


@cbv(student_router)
class Student:

    mongo_db = database

    @student_router.get("/student/{student_id}")
    async def get_student(self, student_id: str) -> StudentModel:
        return await StudentManager.retrieve(mongo_db=self.mongo_db, obj_id=student_id)

    @student_router.post("/student/create")
    async def create_student(self, student_body: StudentModel) -> StudentCreateResponse:
        return await StudentManager.create(mongo_db=self.mongo_db, obj=student_body)
