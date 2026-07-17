"""
salary_engine.py

Generates realistic salary, bonus and increment events.
"""

from __future__ import annotations

import random
from datetime import date
from typing import Dict, List


class SalaryEngine:

    def __init__(self):

        self.increment_probability = 0.08
        self.bonus_probability = 0.03

    def is_salary_day(self, current_date: date) -> bool:
        """
        Salary is usually credited on the 1st of every month.
        """
        return current_date.day == 1

    def generate_salary(
        self,
        user: Dict,
        current_date: date
    ) -> List[Dict]:

        transactions = []

        if not self.is_salary_day(current_date):
            return transactions

        salary = float(user["monthly_income"])

        transactions.append(
            {
                "type": "Income",
                "category": "Salary",
                "amount": round(salary, 2),
                "merchant": "Employer",
                "payment_method": "Bank Transfer",
                "description": "Monthly Salary",
                "date": current_date.isoformat(),
                "recurring": True
            }
        )

        if random.random() < self.increment_probability:

            increment = random.uniform(0.05, 0.15)

            increase = salary * increment

            transactions.append(
                {
                    "type": "Income",
                    "category": "Salary Increment",
                    "amount": round(increase, 2),
                    "merchant": "Employer",
                    "payment_method": "Bank Transfer",
                    "description": "Annual Increment",
                    "date": current_date.isoformat(),
                    "recurring": False
                }
            )

        if random.random() < self.bonus_probability:

            bonus = salary * random.uniform(0.20, 1.00)

            transactions.append(
                {
                    "type": "Income",
                    "category": "Bonus",
                    "amount": round(bonus, 2),
                    "merchant": "Employer",
                    "payment_method": "Bank Transfer",
                    "description": "Performance Bonus",
                    "date": current_date.isoformat(),
                    "recurring": False
                }
            )

        return transactions
    