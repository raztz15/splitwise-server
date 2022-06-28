
from bson.objectid import ObjectId
from pydantic import Field

from .camel_case_model import CamelCaseModel
from .py_objectId import PyObjectId


class Group(CamelCaseModel):
    id: PyObjectId = Field(default=PyObjectId, alias="_id")
    name: str
    participants: list = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
