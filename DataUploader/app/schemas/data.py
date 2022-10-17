from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, PositiveInt


class Statuses(str, Enum):
    OK = "OK"


class TransactionSchema(BaseModel):
    datetime: datetime
    payment: Decimal
    mcc: PositiveInt | None = None  # category code
    
    card: str = ""
    category: str = ""
    description: str = ""

    class Config:
        frozen = True
