from motor import motor_asyncio

from app.core.config import config

client = motor_asyncio.AsyncIOMotorClient(config.MONGO.DB_URL)

database = client[config.MONGO.DB_DATABASE]

student_collection = database.get_collection("students_collection")
