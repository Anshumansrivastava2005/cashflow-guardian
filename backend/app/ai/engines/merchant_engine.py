"""
merchant_engine.py

Loads merchant, category and payment method configuration
and provides realistic merchant selection for the simulator.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Dict, List


# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config" / "india"


def load_json(filename: str):

    path = CONFIG_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


MERCHANTS = load_json("merchants.json")

CATEGORIES = load_json("categories.json")

PAYMENT_METHODS = load_json("payment_methods.json")


# ----------------------------------------------------------
# Merchant Engine
# ----------------------------------------------------------


class MerchantEngine:

    def __init__(self):

        self.merchants = MERCHANTS
        self.categories = CATEGORIES
        self.payment_methods = PAYMENT_METHODS

    # ------------------------------------------------------

    def get_expense_categories(self) -> List[str]:

        return self.categories["Expense"]

    # ------------------------------------------------------

    def get_income_categories(self) -> List[str]:

        return self.categories["Income"]

    # ------------------------------------------------------

    def random_payment_method(self) -> str:

        weights = {
            "UPI": 0.45,
            "Debit Card": 0.20,
            "Credit Card": 0.18,
            "Cash": 0.12,
            "Net Banking": 0.05
        }

        methods = list(weights.keys())

        probabilities = list(weights.values())

        return random.choices(
            methods,
            weights=probabilities,
            k=1
        )[0]

    # ------------------------------------------------------

    def random_expense(self) -> Dict:

        category = random.choice(
            self.get_expense_categories()
        )

        merchant = random.choice(
            self.merchants.get(category, ["Unknown"])
        )

        return {
            "type": "Expense",
            "category": category,
            "merchant": merchant,
            "payment_method": self.random_payment_method()
        }

    # ------------------------------------------------------

    def random_income(self) -> Dict:

        category = random.choice(
            self.get_income_categories()
        )

        merchant = "Employer"

        if category == "Investment":
            merchant = random.choice(
                [
                    "Groww",
                    "Zerodha",
                    "Upstox",
                    "Angel One"
                ]
            )

        elif category == "Business":
            merchant = "Business Client"

        elif category == "Freelancing":
            merchant = "Freelance Client"

        return {
            "type": "Income",
            "category": category,
            "merchant": merchant,
            "payment_method": "Bank Transfer"
        }

    # ------------------------------------------------------

    def random_transaction(self) -> Dict:

        if random.random() < 0.85:
            return self.random_expense()

        return self.random_income()