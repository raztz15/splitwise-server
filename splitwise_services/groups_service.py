from bson.objectid import ObjectId
from fastapi import HTTPException

from app_config import GROUPS_COLLECTIONS_NAME
from models.py_objectId import PyObjectId
from splitwise_services import CollectionService
from models import Group, User


class GroupService(CollectionService):
    def __init__(self):
        CollectionService.__init__(self, GROUPS_COLLECTIONS_NAME, Group)

    def get_groups_of_user(self, user_id: str):
        print(user_id)
        # data = list(self.collection.find({"participants": ObjectId(user_id)}, {'participants': 0}))
        cursor = list(self.collection.find({"participants": ObjectId(user_id)}, {'participants': 0}))
        for doc in cursor:
            doc['_id'] = str(doc['_id'])
            # print(doc['_id'])
        print(cursor)
        return cursor

    def get_group_by_name(self, group_name: str) -> Group:
        return self.get_by_field("name", group_name)

    def add_user_to_group(self, user: User):
        return self.update_by_field("Groups", "participants", {"participants": user})

    def get_group_by_id(self, group_id: str) -> Group:
        return self.get_by_id(group_id)

    # def get_group_by_field(self, field_name, field_value):
        # return self.get_by_field(field_name, field_value)
