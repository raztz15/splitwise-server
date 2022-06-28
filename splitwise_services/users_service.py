from bson import ObjectId

from app_config import USERS_COLLECTIONS_NAME
from splitwise_services import CollectionService
from models import User


class UserService(CollectionService):
    def __init__(self):
        super().__init__(USERS_COLLECTIONS_NAME, User)

    def get_by_username(self, username: str) -> User:
        return self.get_by_field("username", username)

    def get_by_email(self, email: str) -> User:
        return self.get_by_field("email", email)

    def delete_by_username(self, username):
        return self.delete_by_field("username", username)

    def update_by_username(self, username, update):
        return self.update_by_field("username", username, update)

    def get_by_username_and_password(self, username: str, password: str) -> User:
        return self.get_by_fields("username", username, "password", password)

    def get_user_by_id(self, user_id):
        # print(user_id)
        # _id = self.collection.insert({"username": "magen"})
        # print(_id)
        # print(user.username)
        user = self.get_by_id(user_id)
        return user
