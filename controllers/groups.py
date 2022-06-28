from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, Query

from models.group_request import GroupRequest
from splitwise_services import GroupService, UserService
from models import Group, User


class GroupsRouter(APIRouter):
    def __init__(self, groups_service: GroupService):
        super().__init__()
        self.groups_service = groups_service
        # self.users_service = users_service
        self.add_api_route(
            "/",
            endpoint=self.add_group,
            methods=["post"]
        )
        self.add_api_route(
            "/{group_id}",
            endpoint=self.delete_group,
            methods=["delete"]
        )
        self.add_api_route(
            "/{group_id}",
            endpoint=self.update_group,
            methods=["put"]
        )
        self.add_api_route(
            "/{group_id}",
            endpoint=self.get_group_by_id,
            methods=["get"]
        )
        self.add_api_route(
            "/",
            endpoint=self.get_all_groups,
            methods=["get"]
        )

    def add_group(self,  group_request: GroupRequest):
        print(group_request)
        group = group_request.group_data
        user_id = group_request.user_id
        group.participants.append(ObjectId(user_id))
        return self.groups_service.add(group.dict(exclude_unset=True))

    def delete_group(self, group_id) -> bool:
        return self.groups_service.delete(group_id)

    def update_group(self, group_id: str, update=Body(...)):
        updates_succeeded = self.groups_service.update(group_id, update)
        if not updates_succeeded:
            raise HTTPException(status_code=404, detail="group update failed")

    def get_all_groups(self,
                       name: str = Query(None, alias="name")):
        all_groups = self.groups_service.get_all()
        if name:
            all_groups = [group for group in all_groups if str(group.name).lower() == name.lower()]

        print(all_groups)
        return all_groups

    def get_group_by_id(self, group_id: str):
        group = self.groups_service.get_group_by_id(group_id)
        print(group)
        return group

    # def get_group_by_field(self, group_id: str):
        # return self.groups_service.get_group_by_field(group_id)