"""
loader.py

Loads users and transactions from SQLite
for AI feature engineering and model training.
"""

from __future__ import annotations

import pandas as pd

from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.models.user import User


class DatabaseLoader:

    def __init__(self, db: Session):

        self.db = db

    # -----------------------------------------------------

    def users(self):

        return self.db.query(User).all()

    # -----------------------------------------------------

    def transactions(self):

        return self.db.query(Transaction).all()

    # -----------------------------------------------------

    def user_transactions(
        self,
        user_id: int
    ):

        return (

            self.db.query(Transaction)

            .filter(Transaction.user_id == user_id)

            .all()

        )

    # -----------------------------------------------------

    def dataframe(
        self,
        user_id: int | None = None
    ):

        if user_id is None:

            transactions = self.transactions()

        else:

            transactions = self.user_transactions(
                user_id
            )

        data = []

        for transaction in transactions:

            data.append({

                "user_id": transaction.user_id,

                "type": transaction.type,

                "category": transaction.category,

                "amount": transaction.amount,

                "merchant": transaction.merchant,

                "payment_method": transaction.payment_method,

                "description": transaction.description,

                "date": transaction.date,

                "recurring": transaction.recurring

            })

        return pd.DataFrame(data)