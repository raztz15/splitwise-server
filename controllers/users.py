from typing import Optional

import bson
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, Query
from splitwise_services import UserService, GroupService
from models import User, Group


class UsersRouter(APIRouter):
    def __init__(self, user_service: UserService):
        super().__init__()
        self.user_service = user_service
        # self.add_api_route(
        #     "/{username}",
        #     endpoint=self.get_by_username,
        #     methods=["get"]
        # )
        self.add_api_route(
            "/",
            endpoint=self.get_all_users,
            methods=["get"]
        )
        self.add_api_route(
            "/",
            endpoint=self.add_user,
            methods=["post"]
        )
        self.add_api_route(
            "/{username}",
            endpoint=self.delete_user,
            methods=["delete"]
        )
        self.add_api_route(
            "/{username}",
            endpoint=self.update_user,
            methods=["put"]
        )
        self.add_api_route(
            "/",
            endpoint=self.get_by_username_and_password,
            # response_model=User,
            methods=["get"]
        )
        # self.add_api_route(
        #     "/{email}",
        #     endpoint=self.get_by_email,
        #     methods=["get"]
        # )
        self.add_api_route(
            "/{user_id}",
            endpoint=self.get_by_id,
            methods=["get"]
        )

    def get_all_users(self,
                      username: str = None, password: str = None,
                      email: str = Query(None, alias="email")):
        all_users = self.user_service.get_all()
        if email:
            all_users = [user for user in all_users if user.email == email]
        if username and password:
            all_users = [user for user in all_users if user.username == username
                         and user.password == password]
        return all_users

    def add_user(self, user: User):
        return self.user_service.add(user.dict(exclude_unset=True))

    def delete_user(self, username) -> bool:
        return self.user_service.delete_by_username(username)

    def update_user(self, username: str, update=Body(...)):
        update_succeeded = self.user_service.update_by_username(username, update)
        if not update_succeeded:
            raise HTTPException(status_code=400, detail="user update failed")

    def get_by_username_and_password(self,
                                     username: str = Query(None, alias="username"),
                                     password: str = Query(None, alias="password")):
        user = self.user_service.get_by_username_and_password(username, password)
        if username:
            print(username)
            user = []
        return self.user_service.get_by_username_and_password(username, password)

    def get_by_id(self, user_id: str):
        user = self.user_service.get_user_by_id(user_id)
        group = GroupService()
        group_of_user = group.get_groups_of_user(user_id)
        return user, group_of_user


