from pydantic import BaseModel


class TransactionCreate(BaseModel):

    type: str
    category: str
    amount: float
    description: str
    date: str

    payment_method: str
    merchant: str
    recurring: bool


class TransactionResponse(BaseModel):

    id: int
    user_id: int

    type: str
    category: str
    amount: float
    description: str
    date: str

    payment_method: str
    merchant: str
    recurring: bool

    class Config:
        from_attributes = True