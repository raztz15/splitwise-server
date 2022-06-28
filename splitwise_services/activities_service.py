from bson import ObjectId

from app_config import ACTIVITIES_COLLECTIONS_NAME
from models.activity import Activity
from splitwise_services import CollectionService


class ActivitiesService(CollectionService):
    def __init__(self):
        CollectionService.__init__(self, ACTIVITIES_COLLECTIONS_NAME, Activity)

    def get_activity_by_user(self, user_id):
        return list(self.collection.find({"description": user_id}))
