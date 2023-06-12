from app.managers.mongo.base_manager import BaseMongoManager
from app.core.schema.student_model import StudentModel
from app.core.schema.response_model import StudentCreateResponse


class StudentManager(BaseMongoManager[StudentModel, StudentCreateResponse]):
    DetailModel = StudentModel
    CreateModel = StudentCreateResponse
    collection = "student"

