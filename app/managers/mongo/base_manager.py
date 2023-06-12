from typing import Generic

from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from bson.objectid import ObjectId

from app.core.types.common_types import (
    DetailModelType,
    CreateModelType,
)


class BaseMongoManager(Generic[DetailModelType, CreateModelType]):

    collection: str
    DetailModel: BaseModel
    CreateModel: BaseModel

    @classmethod
    def get_collection(cls, mongo_db: AsyncIOMotorDatabase) -> AsyncIOMotorCollection:
        return mongo_db.get_collection(cls.collection)

    @classmethod
    async def retrieve(cls, mongo_db: AsyncIOMotorDatabase, obj_id: str) -> DetailModelType:
        """Retrieve object by id"""
        collection: AsyncIOMotorCollection = cls.get_collection(mongo_db)

        if record := await collection.find_one({"_id": ObjectId(obj_id)}):
            return cls.DetailModel.parse_obj(record)

    @classmethod
    async def create(cls, mongo_db: AsyncIOMotorDatabase, obj: DetailModelType) -> CreateModelType:
        collection: AsyncIOMotorCollection = cls.get_collection(mongo_db)

        result = await collection.insert_one(obj.dict())
        return cls.CreateModel.parse_obj({"object_id": str(result.inserted_id)})
