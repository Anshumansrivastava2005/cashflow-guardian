"""
predictor.py

Loads the trained AI model and predicts
financial risk for users.
"""

from pathlib import Path

import joblib
import pandas as pd

from app.ai.feature_engine import FeatureEngine


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR.parent.parent /
    "ml_models" /
    "cashflow_guardian.pkl"
)


class Predictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.feature_engine = FeatureEngine()

    # ---------------------------------------------------------

    def build_features(self, user_id: int):

        df = self.feature_engine.build_dataset()

        row = df[
            df["user_id"] == user_id
        ]

        if row.empty:

            raise ValueError(
                f"User {user_id} not found."
            )

        return row

    # ---------------------------------------------------------

    def predict(self, user_id: int):

        row = self.build_features(user_id)

        X = row.drop(
            columns=[
                "user_id"
            ]
        )

        prediction = self.model.predict(X)[0]

        probability = self.model.predict_proba(X)[0]

        confidence = float(
            round(
               max(probability) * 100,
               2
            )
        )

        risk = (
            "High Risk"
            if prediction == 1
            else "Low Risk"
        )

        return {

            "user_id": user_id,

            "prediction": risk,

            "confidence": confidence

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    predictor = Predictor()

    print()

    print(
        predictor.predict(1)
    )