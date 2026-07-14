from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.auth import get_current_user
from app.database.database import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


def get_logged_in_user(current_user: str, db: Session):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ---------------- CREATE ---------------- #

@router.post("/")
def add_transaction(
    transaction: TransactionCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    new_transaction = Transaction(
        user_id=user.id,
        type=transaction.type,
        category=transaction.category,
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date,
        payment_method=transaction.payment_method,
        merchant=transaction.merchant,
        recurring=transaction.recurring
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {
        "message": "Transaction Added Successfully",
        "transaction": new_transaction
    }


# ---------------- READ ---------------- #

@router.get("/")
def get_transactions(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    return (
        db.query(Transaction)
        .filter(Transaction.user_id == user.id)
        .all()
    )


# ---------------- READ ONE ---------------- #

@router.get("/{transaction_id}")
def get_transaction(
    transaction_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    transaction = (
        db.query(Transaction)
        .filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user.id
        )
        .first()
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


# ---------------- UPDATE ---------------- #

@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    transaction: TransactionCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    existing = (
        db.query(Transaction)
        .filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user.id
        )
        .first()
    )

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    existing.type = transaction.type
    existing.category = transaction.category
    existing.amount = transaction.amount
    existing.description = transaction.description
    existing.date = transaction.date
    existing.payment_method = transaction.payment_method
    existing.merchant = transaction.merchant
    existing.recurring = transaction.recurring

    db.commit()
    db.refresh(existing)

    return {
        "message": "Transaction Updated Successfully",
        "transaction": existing
    }


# ---------------- DELETE ---------------- #

@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_logged_in_user(current_user, db)

    existing = (
        db.query(Transaction)
        .filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user.id
        )
        .first()
    )

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    db.delete(existing)
    db.commit()

    return {
        "message": "Transaction Deleted Successfully"
    }