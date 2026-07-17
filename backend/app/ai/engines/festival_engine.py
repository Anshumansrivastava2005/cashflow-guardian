"""
festival_engine.py

Generates realistic festival spending spikes.
"""

from __future__ import annotations

import json
import random
from datetime import date
from pathlib import Path
from typing import Dict, List


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config" / "india"


def load_json(filename: str):

    with open(CONFIG_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


MERCHANTS = load_json("merchants.json")


class FestivalEngine:

    def __init__(self):

        self.festivals = {

            "2026-01-01": "New Year",

            "2026-01-26": "Republic Day",

            "2026-03-04": "Holi",

            "2026-08-15": "Independence Day",

            "2026-11-08": "Diwali",

            "2026-12-25": "Christmas"

        }

        self.shopping_range = (3000, 50000)

        self.food_range = (800, 7000)

        self.travel_range = (2000, 30000)

    # --------------------------------------------------------

    def is_festival(self, current_date: date) -> bool:

        return current_date.isoformat() in self.festivals

    # --------------------------------------------------------

    def generate(
        self,
        current_date: date
    ) -> List[Dict]:

        if not self.is_festival(current_date):
            return []

        transactions = []

        # ---------------- Shopping ---------------- #

        transactions.append({

            "type": "Expense",

            "category": "Shopping",

            "merchant": random.choice(
                MERCHANTS["Shopping"]
            ),

            "payment_method": "UPI",

            "amount": round(
                random.uniform(
                    *self.shopping_range
                ),
                2
            ),

            "description": f"{self.festivals[current_date.isoformat()]} Shopping",

            "date": current_date.isoformat(),

            "recurring": False

        })

        # ---------------- Food ---------------- #

        transactions.append({

            "type": "Expense",

            "category": "Food",

            "merchant": random.choice(
                MERCHANTS["Food"]
            ),

            "payment_method": "UPI",

            "amount": round(
                random.uniform(
                    *self.food_range
                ),
                2
            ),

            "description": f"{self.festivals[current_date.isoformat()]} Feast",

            "date": current_date.isoformat(),

            "recurring": False

        })

        # ---------------- Travel ---------------- #

        if random.random() < 0.35:

            transactions.append({

                "type": "Expense",

                "category": "Travel",

                "merchant": random.choice(
                    MERCHANTS["Travel"]
                ),

                "payment_method": "Credit Card",

                "amount": round(
                    random.uniform(
                        *self.travel_range
                    ),
                    2
                ),

                "description": f"{self.festivals[current_date.isoformat()]} Travel",

                "date": current_date.isoformat(),

                "recurring": False

            })

        return transactions