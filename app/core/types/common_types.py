from pydantic import BaseModel
from typing import TypeVar

DetailModelType = TypeVar("DetailModelType", bound=BaseModel)
CreateModelType = TypeVar("CreateModelType", bound=BaseModel)
ListSchemaType = TypeVar("ListSchemaType", bound=BaseModel)
