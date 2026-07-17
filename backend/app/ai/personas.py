"""
personas.py

Loads persona configurations from JSON and generates
realistic virtual users for the Financial Simulator.
"""

from __future__ import annotations

import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List


# ----------------------------------------------------
# Configuration Path
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

CONFIG_DIR = BASE_DIR / "config" / "india"


# ----------------------------------------------------
# Helper
# ----------------------------------------------------

def load_json(filename: str):

    path = CONFIG_DIR / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# ----------------------------------------------------
# Load Configurations
# ----------------------------------------------------

PERSONAS = load_json("personas.json")

CITIES = load_json("cities.json")

PAYMENT_METHODS = load_json("payment_methods.json")


# ----------------------------------------------------
# User Profile
# ----------------------------------------------------

@dataclass
class UserProfile:

    user_id: int

    name: str

    age: int

    occupation: str

    city: str

    lifestyle: str

    monthly_income: float

    preferred_payment: str

    savings_goal: float


# ----------------------------------------------------
# Persona Generator
# ----------------------------------------------------

class PersonaGenerator:

    def __init__(self):

        self.personas = PERSONAS

    def generate_user(self, user_id: int) -> UserProfile:

        persona = random.choice(self.personas)

        income = random.randint(
            persona["salary_min"],
            persona["salary_max"]
        )

        savings_goal = income * random.uniform(
            0.10,
            0.40
        )

        return UserProfile(

            user_id=user_id,

            name=f"User_{user_id}",

            age=random.randint(18, 60),

            occupation=persona["name"],

            city=random.choice(CITIES),

            lifestyle=persona["lifestyle"],

            monthly_income=round(income, 2),

            preferred_payment=random.choice(
                PAYMENT_METHODS
            ),

            savings_goal=round(
                savings_goal,
                2
            )
        )

    def generate_users(
        self,
        count: int
    ) -> List[UserProfile]:

        users = []

        for user_id in range(1, count + 1):

            users.append(
                self.generate_user(user_id)
            )

        return users


# ----------------------------------------------------
# Demo
# ----------------------------------------------------

if __name__ == "__main__":

    generator = PersonaGenerator()

    users = generator.generate_users(5)

    for user in users:

        print(asdict(user))