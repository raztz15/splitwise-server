from bson import ObjectId

from models import Debt
from splitwise_services import CollectionService
from app_config import DEBTS_COLLECTIONS_NAME


class DebtsService(CollectionService):
    def __init__(self):
        CollectionService.__init__(self, DEBTS_COLLECTIONS_NAME, Debt)

    def get_debts_from(self, user_id):
        return list(self.collection.find({"from_id": user_id}))

    def get_debts_to(self, user_id):
        return list(self.collection.find({"to_id": user_id}))

    def get_debt_by_id(self, debt_id) -> Debt:
        return self.get_by_field("_id", ObjectId(debt_id))

