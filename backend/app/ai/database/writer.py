"""
writer.py

Stores generated AI users and transactions
into the application's SQLite database.
"""

from __future__ import annotations

from typing import Dict, List

from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.models.user import User


class DatabaseWriter:

    def __init__(self, db: Session):

        self.db = db

    # -----------------------------------------------------

    def create_user(self, profile: Dict) -> User:

        existing = (
            self.db.query(User)
            .filter(User.email == profile["email"])
            .first()
        )

        if existing:
            return existing

        user = User(

            full_name=profile["name"],

            email=profile["email"],

            password="$SIMULATED_USER$"

        )

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user

    # -----------------------------------------------------

    def create_transaction(
        self,
        user_id: int,
        transaction: Dict
    ):

        row = Transaction(

            user_id=user_id,

            type=transaction["type"],

            category=transaction["category"],

            amount=float(transaction["amount"]),

            description=transaction["description"],

            date=transaction["date"],

            payment_method=transaction["payment_method"],

            merchant=transaction["merchant"],

            recurring=transaction["recurring"]

        )

        self.db.add(row)

    # -----------------------------------------------------

    def create_transactions(
        self,
        user_id: int,
        transactions: List[Dict]
    ):

        for transaction in transactions:

            self.create_transaction(
                user_id=user_id,
                transaction=transaction
            )

        self.db.commit()