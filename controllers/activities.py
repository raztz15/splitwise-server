from fastapi import APIRouter, Query

from models.activity import Activity
from splitwise_services.activities_service import ActivitiesService


class ActivitiesRouter(APIRouter):
    def __init__(self, activities_service: ActivitiesService):
        super().__init__()
        self.activities_service = activities_service
        self.add_api_route(
            "/",
            endpoint=self.add_activity,
            methods=["post"]
        )

        self.add_api_route(
            "/{user_id}",
            endpoint=self.get_activity_by_user,
            methods=["get"]
        )

        self.add_api_route(
            "/",
            endpoint=self.get_all,
            methods=["get"]
        )

    def add_activity(self, activity: Activity):
        return self.activities_service.add(activity.dict(exclude_unset=True))

    def get_activity_by_user(self,
                             username: str = Query(None, alias="username")):
        if username:
            return self.activities_service.get_activity_by_user(username)

    def get_all(self):
        return self.activities_service.get_all()
