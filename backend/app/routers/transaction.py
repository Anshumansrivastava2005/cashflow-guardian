from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate
from app.auth.auth import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


# CREATE
@router.post("/")
def add_transaction(
    transaction: TransactionCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    new_transaction = Transaction(
        user_id=user.id,
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
        "message": "Transaction Added Successfully",
        "transaction": new_transaction
    }


# READ ALL
@router.get("/")
def get_transactions(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    return db.query(Transaction).filter(
        Transaction.user_id == user.id
    ).all()


# READ ONE
@router.get("/{transaction_id}")
def get_transaction(
    transaction_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user.id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


# UPDATE
@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    transaction: TransactionCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    existing = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user.id
    ).first()

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

    db.commit()
    db.refresh(existing)

    return {
        "message": "Transaction Updated Successfully",
        "transaction": existing
    }


# DELETE
@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == current_user
    ).first()

    existing = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == user.id
    ).first()

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