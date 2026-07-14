from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/")
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):

    new_transaction = Transaction(
        user_id=1,          # Temporary
        type=transaction.type,
        category=transaction.category,
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {
        "message": "Transaction Added",
        "id": new_transaction.id
    }


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):

    transactions = db.query(Transaction).all()

    return transactions