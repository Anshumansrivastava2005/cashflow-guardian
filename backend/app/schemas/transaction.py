from datetime import date

from pydantic import BaseModel


class TransactionCreate(BaseModel):

    type: str
    category: str
    amount: float
    description: str
    date: date


class TransactionResponse(BaseModel):

    id: int
    user_id: int

    type: str
    category: str
    amount: float
    description: str
    date: date

    class Config:
        from_attributes = True