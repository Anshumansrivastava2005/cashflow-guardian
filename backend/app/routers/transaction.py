from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


# CREATE
@router.post("/")
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):

    new_transaction = Transaction(
        user_id=1,   # Temporary (JWT will replace this later)
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


# READ
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()

    return transactions


# READ BY ID
@router.get("/{transaction_id}")
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
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
    db: Session = Depends(get_db)
):

    existing = db.query(Transaction).filter(
        Transaction.id == transaction_id
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
    db: Session = Depends(get_db)
):

    existing = db.query(Transaction).filter(
        Transaction.id == transaction_id
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