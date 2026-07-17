"""
feature_engine.py

Builds ML-ready features from simulated financial data.
"""

from __future__ import annotations

import pandas as pd

from app.database.database import SessionLocal
from app.models.sim_user import SimUser
from app.models.sim_transaction import SimTransaction


class FeatureEngine:

    def __init__(self):

        self.db = SessionLocal()

    # ---------------------------------------------------------

    def close(self):

        self.db.close()

    # ---------------------------------------------------------

    def load_transactions(self):

        return self.db.query(
            SimTransaction
        ).all()

    # ---------------------------------------------------------

    def build_dataset(self):

        users = self.db.query(
            SimUser
        ).all()

        dataset = []

        for user in users:

            transactions = self.db.query(
                SimTransaction
            ).filter(
                SimTransaction.sim_user_id == user.id
            ).all()

            income = 0.0
            expense = 0.0

            food = 0.0
            shopping = 0.0
            travel = 0.0
            bills = 0.0
            entertainment = 0.0
            healthcare = 0.0

            recurring = 0
            total_transactions = len(transactions)

            for t in transactions:

                if t.type == "Income":
                    income += t.amount
                else:
                    expense += t.amount

                if t.recurring:
                    recurring += 1

                category = t.category.lower()

                if category == "food":
                    food += t.amount

                elif category == "shopping":
                    shopping += t.amount

                elif category == "travel":
                    travel += t.amount

                elif category in (
                    "bills",
                    "utilities"
                ):
                    bills += t.amount

                elif category == "entertainment":
                    entertainment += t.amount

                elif category in (
                    "health",
                    "healthcare"
                ):
                    healthcare += t.amount

            savings = income - expense

            savings_rate = (
                savings / income
                if income > 0
                else 0
            )

            recurring_ratio = (
                recurring / total_transactions
                if total_transactions > 0
                else 0
            )

            dataset.append({

                "user_id": user.id,

                "age": user.age,

                "monthly_income": user.monthly_income,

                "income": round(income, 2),

                "expense": round(expense, 2),

                "savings": round(savings, 2),

                "savings_rate": round(
                    savings_rate,
                    4
                ),

                "food_spend": round(food, 2),

                "shopping_spend": round(
                    shopping,
                    2
                ),

                "travel_spend": round(
                    travel,
                    2
                ),

                "bills_spend": round(
                    bills,
                    2
                ),

                "entertainment_spend": round(
                    entertainment,
                    2
                ),

                "healthcare_spend": round(
                    healthcare,
                    2
                ),

                "transaction_count": total_transactions,

                "recurring_ratio": round(
                    recurring_ratio,
                    4
                )

            })

        return pd.DataFrame(dataset)


# ---------------------------------------------------------

if __name__ == "__main__":

    engine = FeatureEngine()

    df = engine.build_dataset()

    print(df.head())

    print()

    print(df.shape)

    engine.close()