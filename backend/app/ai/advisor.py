"""
advisor.py

Generates personalized financial advice based
on user spending behaviour and AI prediction.
"""

from app.ai.feature_engine import FeatureEngine
from app.ai.predictor import Predictor


class FinancialAdvisor:

    def __init__(self):

        self.predictor = Predictor()

        self.feature_engine = FeatureEngine()

    # ---------------------------------------------------------

    def get_features(self, user_id: int):

        df = self.feature_engine.build_dataset()

        row = df[
            df["user_id"] == user_id
        ]

        if row.empty:
            raise ValueError("User not found")

        return row.iloc[0]

    # ---------------------------------------------------------

    def advise(self, user_id: int):

        prediction = self.predictor.predict(user_id)

        features = self.get_features(user_id)

        advice = []

        if prediction["prediction"] == "High Risk":

            advice.append(
                "Increase your monthly savings."
            )

        if features["shopping_spend"] > 15000:

            advice.append(
                "Reduce shopping expenses."
            )

        if features["food_spend"] > 8000:

            advice.append(
                "Reduce restaurant and food delivery spending."
            )

        if features["travel_spend"] > 10000:

            advice.append(
                "Plan travel expenses more carefully."
            )

        if features["entertainment_spend"] > 5000:

            advice.append(
                "Lower entertainment expenses."
            )

        if features["healthcare_spend"] > 10000:

            advice.append(
                "Maintain a dedicated emergency medical fund."
            )

        if features["recurring_ratio"] > 0.30:

            advice.append(
                "Review recurring subscriptions."
            )

        if features["savings_rate"] < 0.20:

            advice.append(
                "Aim to save at least 20% of your income every month."
            )

        if len(advice) == 0:

            advice.append(
                "Your financial habits look healthy. Keep it up!"
            )

        return {

            "prediction": prediction,

            "advice": advice

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    advisor = FinancialAdvisor()

    result = advisor.advise(1)

    print()

    print(result)