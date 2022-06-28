from datetime import datetime
import json

from .camel_case_model import CamelCaseModel


class Activity(CamelCaseModel):
    description: str
    date: datetime = json.dumps(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
