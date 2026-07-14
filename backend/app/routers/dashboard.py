from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.auth.auth import get_current_user

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def home():
    return {
        "message": "Dashboard API Working"
    }


@router.get("/summary")
def dashboard_summary(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    transactions = db.query(Transaction).filter(
        Transaction.user_id == user.id
    ).all()

    total_income = 0
    total_expense = 0

    for transaction in transactions:

        if transaction.type.lower() == "income":
            total_income += transaction.amount

        elif transaction.type.lower() == "expense":
            total_expense += transaction.amount

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "current_balance": total_income - total_expense,
        "total_transactions": len(transactions)
    }