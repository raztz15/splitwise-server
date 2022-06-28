from fastapi import APIRouter, Query, Body, HTTPException

from models import Debt
from splitwise_services import DebtsService


class DebtsRouter(APIRouter):
    def __init__(self, debts_service: DebtsService):
        super().__init__()
        self.debts_service = debts_service
        self.add_api_route(
            "/",
            endpoint=self.add_debt,
            methods=["post"]
        )
        self.add_api_route(
            "/",
            endpoint=self.get_all_debts,
            methods=["get"]
        )
        self.add_api_route(
            "/{debt_id}",
            endpoint=self.get_one_debt,
            methods=["get"]
        )
        self.add_api_route(
            "/{debt_id}",
            endpoint=self.update_debt,
            methods=["put"]
        )
        self.add_api_route(
            "/{debt_id}",
            endpoint=self.delete_debt,
            methods=["delete"]
        )

    def add_debt(self, debt: Debt):
        return self.debts_service.add(debt.dict(exclude_unset=True))

    def get_all_debts(self,
                      debts_from: str = Query(None, alias="from"),
                      debts_to: str = Query(None, alias="to"),
                      description: str = Query(None, alias="desc")):
        all_debts = self.debts_service.get_all()
        if debts_from:
            all_debts = [debt for debt in all_debts if debt.from_user == debts_from]
        if debts_to:
            all_debts = [debt for debt in all_debts if debt.to_user == debts_to]
        if description:
            all_debts = [debt for debt in all_debts if debt.description == description]
        return all_debts

    def get_one_debt(self, debt_id):
        return self.debts_service.get_debt_by_id(debt_id)

    def update_debt(self, debt_id: str, update=Body(...)):
        self.debts_service.update(debt_id, update)

    def delete_debt(self, debt_id):
        update_succeeded = self.debts_service.delete(debt_id)
        if not update_succeeded:
            raise HTTPException(status_code=400, detail="debt update failed")

