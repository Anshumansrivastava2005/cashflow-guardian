from collections import defaultdict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth.auth import get_current_user
from app.database.database import get_db
from app.models.transaction import Transaction
from app.models.user import User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


def get_logged_in_user(current_user: str, db: Session):
    user = db.query(User).filter(User.email == current_user).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/")
def dashboard_home():
    return {
        "message": "Dashboard API Working"
    }


@router.get("/summary")
def dashboard_summary(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    income = (
        db.query(func.sum(Transaction.amount))
        .filter(
            Transaction.user_id == user.id,
            Transaction.type == "Income"
        )
        .scalar()
    ) or 0

    expense = (
        db.query(func.sum(Transaction.amount))
        .filter(
            Transaction.user_id == user.id,
            Transaction.type == "Expense"
        )
        .scalar()
    ) or 0

    total = (
        db.query(func.count(Transaction.id))
        .filter(Transaction.user_id == user.id)
        .scalar()
    )

    return {
        "total_income": income,
        "total_expense": expense,
        "current_balance": income - expense,
        "total_transactions": total
    }


@router.get("/recent")
def recent_transactions(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    return (
        db.query(Transaction)
        .filter(Transaction.user_id == user.id)
        .order_by(Transaction.id.desc())
        .limit(5)
        .all()
    )


@router.get("/category")
def category_summary(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    rows = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount)
        )
        .filter(
            Transaction.user_id == user.id,
            Transaction.type == "Expense"
        )
        .group_by(Transaction.category)
        .all()
    )

    result = []

    for category, amount in rows:
        result.append({
            "category": category,
            "amount": amount
        })

    return result


@router.get("/monthly")
def monthly_summary(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    transactions = (
        db.query(Transaction)
        .filter(Transaction.user_id == user.id)
        .all()
    )

    monthly = defaultdict(
        lambda: {
            "income": 0,
            "expense": 0
        }
    )

    for transaction in transactions:

        month = transaction.date.strftime("%Y-%m")

        if transaction.type == "Income":
            monthly[month]["income"] += transaction.amount
        else:
            monthly[month]["expense"] += transaction.amount

    response = []

    for month in sorted(monthly.keys()):

        income = monthly[month]["income"]
        expense = monthly[month]["expense"]

        response.append({
            "month": month,
            "income": income,
            "expense": expense,
            "balance": income - expense
        })

    return response


@router.get("/trend")
def cashflow_trend(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    transactions = (
        db.query(Transaction)
        .filter(Transaction.user_id == user.id)
        .order_by(Transaction.date)
        .all()
    )

    balance = 0

    trend = []

    for transaction in transactions:

        if transaction.type == "Income":
            balance += transaction.amount
        else:
            balance -= transaction.amount

        trend.append({
            "date": transaction.date,
            "balance": balance
        })

    return trend