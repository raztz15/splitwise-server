from pydantic import Field

import bson

from bson import ObjectId

from models import CamelCaseModel
from models.py_objectId import PyObjectId


class User(CamelCaseModel):
    id: PyObjectId = Field(default=PyObjectId, alias='_id')
    username: str
    email: str
    phone: str
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

