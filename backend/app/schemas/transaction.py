from pydantic import BaseModel


class TransactionCreate(BaseModel):
    type: str
    category: str
    amount: float
    description: str
    date: str


class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True