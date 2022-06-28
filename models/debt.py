from .camel_case_model import CamelCaseModel


class Debt(CamelCaseModel):
    description: str
    amount: float
    from_user: str
    to_user: str
