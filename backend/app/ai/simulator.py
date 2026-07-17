"""
simulator.py

Main AI simulator responsible for generating
large volumes of realistic financial data and
storing them inside the simulation database.
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from typing import List

from app.ai.personas import PersonaGenerator
from app.ai.engines.transaction_engine import TransactionEngine

from app.database.database import SessionLocal

from app.models.sim_user import SimUser
from app.models.sim_transaction import SimTransaction


class FinancialSimulator:

    def __init__(self):

        self.db = SessionLocal()

        self.persona_generator = PersonaGenerator()

        self.transaction_engine = TransactionEngine()

    # ---------------------------------------------------------

    def close(self):

        self.db.close()

    # ---------------------------------------------------------

    def create_sim_user(
        self,
        profile
    ) -> SimUser:

        user = SimUser(

            full_name=profile.name,

            age=profile.age,

            gender="Unknown",

            city=profile.city,

            occupation=profile.occupation,

            monthly_income=profile.monthly_income,

            lifestyle=profile.lifestyle,

            risk_profile="Medium"

        )

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user

    # ---------------------------------------------------------

    def create_transaction(
        self,
        user_id: int,
        transaction: dict
    ):

        db_transaction = SimTransaction(

            sim_user_id=user_id,

            type=transaction["type"],

            category=transaction["category"],

            amount=transaction["amount"],

            description=transaction.get(
                "description",
                ""
            ),

            date=str(
                transaction["date"]
            ),

            payment_method=transaction.get(
                "payment_method",
                "UPI"
            ),

            merchant=transaction.get(
                "merchant",
                "Unknown"
            ),

            recurring=transaction.get(
                "recurring",
                False
            )

        )

        self.db.add(db_transaction)

    # ---------------------------------------------------------

    def generate_user_transactions(
        self,
        sim_user: SimUser,
        profile,
        year: int
    ):

        user_dict = asdict(profile)

        transactions = self.transaction_engine.generate_year(

            user=user_dict,

            year=year

        )

        for transaction in transactions:

            self.create_transaction(

                user_id=sim_user.id,

                transaction=transaction

            )

        self.db.commit()

            # ---------------------------------------------------------

    def simulate_user(
        self,
        profile,
        year: int
    ) -> SimUser:

        sim_user = self.create_sim_user(profile)

        self.generate_user_transactions(
            sim_user=sim_user,
            profile=profile,
            year=year
        )

        return sim_user

    # ---------------------------------------------------------

    def simulate(
        self,
        users: int = 100,
        year: int = datetime.now().year
    ):

        profiles = self.persona_generator.generate_users(
            users
        )

        created_users = []

        print()

        print("=" * 60)
        print("Financial Data Simulation Started")
        print("=" * 60)

        for index, profile in enumerate(
            profiles,
            start=1
        ):

            sim_user = self.simulate_user(
                profile=profile,
                year=year
            )

            created_users.append(sim_user)

            print(
                f"[{index}/{users}] "
                f"{profile.name} "
                f"completed."
            )

        print()
        print("=" * 60)
        print("Simulation Completed")
        print("=" * 60)

        return created_users

    # ---------------------------------------------------------

    def statistics(self):

        total_users = self.db.query(
            SimUser
        ).count()

        total_transactions = self.db.query(
            SimTransaction
        ).count()

        total_income = self.db.query(
            SimTransaction
        ).filter(
            SimTransaction.type == "Income"
        ).count()

        total_expense = self.db.query(
            SimTransaction
        ).filter(
            SimTransaction.type == "Expense"
        ).count()

        print()

        print("=" * 60)
        print("Simulation Statistics")
        print("=" * 60)

        print(f"Users              : {total_users}")
        print(f"Transactions       : {total_transactions}")
        print(f"Income Entries     : {total_income}")
        print(f"Expense Entries    : {total_expense}")

        print("=" * 60)

    # ---------------------------------------------------------

    def reset_database(self):

        self.db.query(
            SimTransaction
        ).delete()

        self.db.query(
            SimUser
        ).delete()

        self.db.commit()

        print()

        print("Simulation database cleared.")

        # ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    simulator = FinancialSimulator()

    try:

        simulator.reset_database()

        simulator.simulate(

            users=100,

            year=2026

        )

        simulator.statistics()

    finally:

        simulator.close()


if __name__ == "__main__":

    main()