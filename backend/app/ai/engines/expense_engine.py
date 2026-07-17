"""
expense_engine.py

Generates realistic expense transactions based on category.
"""

from __future__ import annotations

import random
from datetime import date
from typing import Dict

from app.ai.engines.merchant_engine import MerchantEngine


class ExpenseEngine:

    def __init__(self):

        self.merchant_engine = MerchantEngine()

        self.category_rules = {
            "Food": {
                "min": 120,
                "max": 800,
                "description": [
                    "Breakfast",
                    "Lunch",
                    "Dinner",
                    "Snacks",
                    "Coffee"
                ]
            },

            "Shopping": {
                "min": 500,
                "max": 15000,
                "description": [
                    "Online Shopping",
                    "Clothing",
                    "Electronics",
                    "Accessories"
                ]
            },

            "Travel": {
                "min": 80,
                "max": 4000,
                "description": [
                    "Cab Ride",
                    "Metro",
                    "Train Ticket",
                    "Flight",
                    "Bus Ticket"
                ]
            },

            "Bills": {
                "min": 500,
                "max": 6000,
                "description": [
                    "Electricity Bill",
                    "Internet Bill",
                    "Water Bill",
                    "Mobile Recharge"
                ]
            },

            "Entertainment": {
                "min": 200,
                "max": 3500,
                "description": [
                    "Movie",
                    "Gaming",
                    "Concert",
                    "Streaming"
                ]
            },

            "Fuel": {
                "min": 400,
                "max": 3500,
                "description": [
                    "Petrol",
                    "Diesel",
                    "Fuel Refill"
                ]
            },

            "Medical": {
                "min": 250,
                "max": 12000,
                "description": [
                    "Medicine",
                    "Doctor Visit",
                    "Health Checkup"
                ]
            },

            "Education": {
                "min": 500,
                "max": 25000,
                "description": [
                    "Course Purchase",
                    "Books",
                    "College Fees"
                ]
            },

            "Insurance": {
                "min": 1000,
                "max": 30000,
                "description": [
                    "Insurance Premium"
                ]
            }
        }

    def generate_expense(
        self,
        current_date: date
    ) -> Dict:

        transaction = self.merchant_engine.random_expense()

        category = transaction["category"]

        rule = self.category_rules.get(category)

        if rule is None:
            amount = random.randint(100, 1000)
            description = "Expense"

        else:

            amount = round(
                random.uniform(
                    rule["min"],
                    rule["max"]
                ),
                2
            )

            description = random.choice(
                rule["description"]
            )

        transaction.update({

            "amount": amount,

            "description": description,

            "date": current_date.isoformat(),

            "recurring": False

        })

        return transaction