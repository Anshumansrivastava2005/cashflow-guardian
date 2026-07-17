"""
transaction_engine.py

Combines all AI engines to generate realistic
daily financial transactions for a single user.
"""

from __future__ import annotations

import random
from datetime import date
from typing import Dict, List

from app.ai.engines.salary_engine import SalaryEngine
from app.ai.engines.expense_engine import ExpenseEngine
from app.ai.engines.subscription_engine import SubscriptionEngine
from app.ai.engines.festival_engine import FestivalEngine
from app.ai.engines.emergency_engine import EmergencyEngine


class TransactionEngine:

    def __init__(self):

        self.salary_engine = SalaryEngine()

        self.expense_engine = ExpenseEngine()

        self.subscription_engine = SubscriptionEngine()

        self.festival_engine = FestivalEngine()

        self.emergency_engine = EmergencyEngine()

    # ---------------------------------------------------------

    def generate_daily_transactions(
        self,
        user: Dict,
        current_date: date
    ) -> List[Dict]:

        transactions: List[Dict] = []

        # --------------------------------------------
        # Salary
        # --------------------------------------------

        transactions.extend(
            self.salary_engine.generate_salary(
                user=user,
                current_date=current_date
            )
        )

        # --------------------------------------------
        # Recurring Subscriptions
        # --------------------------------------------

        transactions.extend(
            self.subscription_engine.generate(
                current_date=current_date
            )
        )

        # --------------------------------------------
        # Festivals
        # --------------------------------------------

        transactions.extend(
            self.festival_engine.generate(
                current_date=current_date
            )
        )

        # --------------------------------------------
        # Emergencies
        # --------------------------------------------

        transactions.extend(
            self.emergency_engine.generate(
                current_date=current_date
            )
        )

        # --------------------------------------------
        # Daily Expenses
        # --------------------------------------------

        weekday = current_date.weekday()

        if weekday < 5:
            expense_count = random.randint(1, 4)
        else:
            expense_count = random.randint(3, 7)

        for _ in range(expense_count):

            transactions.append(
                self.expense_engine.generate_expense(
                    current_date=current_date
                )
            )

        return transactions

    # ---------------------------------------------------------

    def generate_month(
        self,
        user: Dict,
        year: int,
        month: int
    ) -> List[Dict]:

        from calendar import monthrange

        all_transactions = []

        total_days = monthrange(
            year,
            month
        )[1]

        for day in range(1, total_days + 1):

            current_date = date(
                year,
                month,
                day
            )

            daily = self.generate_daily_transactions(
                user=user,
                current_date=current_date
            )

            all_transactions.extend(daily)

        return all_transactions

    # ---------------------------------------------------------

    def generate_year(
        self,
        user: Dict,
        year: int
    ) -> List[Dict]:

        all_transactions = []

        for month in range(1, 13):

            monthly = self.generate_month(
                user=user,
                year=year,
                month=month
            )

            all_transactions.extend(monthly)

        return all_transactions