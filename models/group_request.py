from models import Group, CamelCaseModel


class GroupRequest(CamelCaseModel):
    group_data: Group
    user_id: str
