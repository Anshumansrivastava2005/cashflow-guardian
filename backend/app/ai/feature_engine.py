import pandas as pd
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class FeatureEngineer:

    def __init__(self, db: Session):
        self.db = db

    def load_transactions(self, user_id: int):

        transactions = (
            self.db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )

        data = []

        for t in transactions:

            data.append({
                "type": t.type,
                "category": t.category,
                "amount": t.amount,
                "merchant": t.merchant,
                "payment_method": t.payment_method,
                "recurring": int(t.recurring),
                "date": t.date
            })

        return pd.DataFrame(data)

    def generate_features(self, user_id: int):

        df = self.load_transactions(user_id)

        if df.empty:
            return None

        income = df[df["type"] == "Income"]["amount"].sum()

        expense = df[df["type"] == "Expense"]["amount"].sum()

        savings = income - expense

        transaction_count = len(df)

        avg_transaction = df["amount"].mean()

        max_transaction = df["amount"].max()

        expense_ratio = 0

        if income > 0:
            expense_ratio = expense / income

        merchant_count = df["merchant"].nunique()

        payment_method_count = df["payment_method"].nunique()

        recurring_count = df["recurring"].sum()

        features = {
            "income": income,
            "expense": expense,
            "savings": savings,
            "expense_ratio": expense_ratio,
            "transaction_count": transaction_count,
            "average_transaction": avg_transaction,
            "largest_transaction": max_transaction,
            "merchant_count": merchant_count,
            "payment_method_count": payment_method_count,
            "recurring_transactions": recurring_count
        }

        return pd.DataFrame([features])