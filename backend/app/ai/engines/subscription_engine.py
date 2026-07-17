"""
subscription_engine.py

Generates recurring monthly subscriptions such as
Netflix, Spotify, Rent, EMI, SIP, Insurance, etc.
"""

from __future__ import annotations

import random
from datetime import date
from typing import Dict, List


class SubscriptionEngine:

    def __init__(self):

        self.subscriptions = [

            {
                "merchant": "Netflix",
                "category": "Entertainment",
                "amount": 649,
                "description": "Netflix Premium",
                "day": 5
            },

            {
                "merchant": "Spotify",
                "category": "Entertainment",
                "amount": 119,
                "description": "Spotify Premium",
                "day": 10
            },

            {
                "merchant": "Amazon Prime",
                "category": "Entertainment",
                "amount": 299,
                "description": "Amazon Prime",
                "day": 12
            },

            {
                "merchant": "Disney+ Hotstar",
                "category": "Entertainment",
                "amount": 149,
                "description": "Disney+ Subscription",
                "day": 15
            },

            {
                "merchant": "Cult.fit",
                "category": "Health",
                "amount": 999,
                "description": "Gym Membership",
                "day": 3
            },

            {
                "merchant": "Landlord",
                "category": "Rent",
                "amount": 15000,
                "description": "Monthly House Rent",
                "day": 1
            },

            {
                "merchant": "HDFC Bank",
                "category": "EMI",
                "amount": 8500,
                "description": "Home Loan EMI",
                "day": 7
            },

            {
                "merchant": "LIC",
                "category": "Insurance",
                "amount": 2500,
                "description": "Insurance Premium",
                "day": 18
            },

            {
                "merchant": "Groww",
                "category": "Investment",
                "amount": 5000,
                "description": "Monthly SIP",
                "day": 2
            }
        ]

    # -------------------------------------------------

    def generate(
        self,
        current_date: date
    ) -> List[Dict]:

        transactions = []

        for subscription in self.subscriptions:

            if current_date.day != subscription["day"]:
                continue

            transaction = {

                "type": "Expense",

                "category": subscription["category"],

                "merchant": subscription["merchant"],

                "payment_method": "Auto Debit",

                "amount": float(subscription["amount"]),

                "description": subscription["description"],

                "date": current_date.isoformat(),

                "recurring": True

            }

            transactions.append(transaction)

        return transactions