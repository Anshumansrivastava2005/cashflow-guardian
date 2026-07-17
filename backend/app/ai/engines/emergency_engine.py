"""
emergency_engine.py

Generates rare emergency expenses such as
hospital bills, vehicle repair, gadget replacement, etc.
"""

from __future__ import annotations

import random
from datetime import date
from typing import Dict, List


class EmergencyEngine:

    def __init__(self):

        self.probability = 0.015

        self.events = [

            {
                "merchant": "Apollo Hospital",
                "category": "Medical",
                "min": 3000,
                "max": 50000,
                "description": "Medical Emergency"
            },

            {
                "merchant": "Fortis Hospital",
                "category": "Medical",
                "min": 5000,
                "max": 100000,
                "description": "Hospital Admission"
            },

            {
                "merchant": "Authorized Service Center",
                "category": "Repair",
                "min": 1000,
                "max": 25000,
                "description": "Laptop Repair"
            },

            {
                "merchant": "Mobile Service Center",
                "category": "Repair",
                "min": 800,
                "max": 18000,
                "description": "Mobile Repair"
            },

            {
                "merchant": "Car Workshop",
                "category": "Vehicle",
                "min": 2000,
                "max": 45000,
                "description": "Car Repair"
            },

            {
                "merchant": "Bike Service Center",
                "category": "Vehicle",
                "min": 500,
                "max": 12000,
                "description": "Bike Repair"
            },

            {
                "merchant": "Croma",
                "category": "Electronics",
                "min": 20000,
                "max": 120000,
                "description": "Laptop Replacement"
            },

            {
                "merchant": "Reliance Digital",
                "category": "Electronics",
                "min": 10000,
                "max": 90000,
                "description": "Mobile Replacement"
            }
        ]

    # -------------------------------------------------------------

    def should_generate(self) -> bool:

        return random.random() < self.probability

    # -------------------------------------------------------------

    def generate(
        self,
        current_date: date
    ) -> List[Dict]:

        if not self.should_generate():
            return []

        event = random.choice(self.events)

        amount = round(
            random.uniform(
                event["min"],
                event["max"]
            ),
            2
        )

        transaction = {

            "type": "Expense",

            "category": event["category"],

            "merchant": event["merchant"],

            "payment_method": random.choice(
                [
                    "UPI",
                    "Credit Card",
                    "Debit Card"
                ]
            ),

            "amount": amount,

            "description": event["description"],

            "date": current_date.isoformat(),

            "recurring": False

        }

        return [transaction]