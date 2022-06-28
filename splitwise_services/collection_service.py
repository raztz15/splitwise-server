from fastapi import HTTPException

from app_config import MONGO_DB_HOST, MONGO_DB_PORT, SPLITWISE_DB_NAME
from pymongo import MongoClient
from bson.objectid import ObjectId
import re


class CollectionService:
    def __init__(self, collection_name, model_class):
        client = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT)
        db = client[SPLITWISE_DB_NAME]
        self.collection = db[collection_name]
        self.model_class = model_class

    def get_all(self):
        return list(map(lambda x: self.model_class(**x), self.collection.find()))

    def get_by_id(self, object_id: str):
        document = self.model_class(**dict(self.collection.find_one({'_id': ObjectId(object_id)})))
        if document is None:
            raise HTTPException(status_code=404, detail="Data is not found")
        return document

    def get_by_field(self, field_name, value):
        obj = self.model_class(**dict(self.collection.find_one({field_name: re.compile(value, re.IGNORECASE)})))
        # print(field_name, value)
        # obj = self.model_class(self.collection.find({field_name: value}))
        return obj

    def get_by_fields(self, field_name1, value1, field_name2, value2):
        return self.model_class(**dict(self.collection.find_one({field_name1: value1, field_name2: value2})))

    def add(self, document: dict):
        return str(self.collection.insert_one(document).inserted_id)

    def update(self, object_id: str, updates: dict):
        return self.collection.update_one({"_id": ObjectId(object_id)}, {"$set": updates})

    def update_by_field(self, field_name, field_value, update: dict):
        return self.collection.update_one({field_name: field_value}, {"$set": update}).modified_count > 0

    def delete(self, object_id: str):
        return self.collection.delete_one({"_id": ObjectId(object_id)}).deleted_count > 0

    def delete_by_field(self, field_name, field_value):
        return self.collection.delete_one({field_name: field_value}).deleted_count > 0

