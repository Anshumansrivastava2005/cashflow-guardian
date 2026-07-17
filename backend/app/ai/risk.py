"""
risk.py

Calculates a financial health score and
assigns a financial risk level.
"""

from app.ai.feature_engine import FeatureEngine
from app.ai.predictor import Predictor


class RiskAnalyzer:

    def __init__(self):

        self.feature_engine = FeatureEngine()
        self.predictor = Predictor()

    # ---------------------------------------------------------

    def get_features(self, user_id: int):

        df = self.feature_engine.build_dataset()

        row = df[df["user_id"] == user_id]

        if row.empty:
            raise ValueError(f"User {user_id} not found.")

        return row.iloc[0]

    # ---------------------------------------------------------

    def calculate_score(self, features):

        score = 100.0

        # Savings Rate
        if features["savings_rate"] < 0.10:
            score -= 40
        elif features["savings_rate"] < 0.20:
            score -= 25
        elif features["savings_rate"] < 0.30:
            score -= 10

        # Shopping
        if features["shopping_spend"] > 30000:
            score -= 15
        elif features["shopping_spend"] > 15000:
            score -= 8

        # Food
        if features["food_spend"] > 15000:
            score -= 10
        elif features["food_spend"] > 8000:
            score -= 5

        # Travel
        if features["travel_spend"] > 20000:
            score -= 10
        elif features["travel_spend"] > 10000:
            score -= 5

        # Entertainment
        if features["entertainment_spend"] > 10000:
            score -= 10
        elif features["entertainment_spend"] > 5000:
            score -= 5

        # Healthcare
        if features["healthcare_spend"] > 15000:
            score -= 5

        # Recurring Expenses
        if features["recurring_ratio"] > 0.50:
            score -= 10
        elif features["recurring_ratio"] > 0.30:
            score -= 5

        score = max(0.0, min(100.0, score))

        return float(round(score, 2))

    # ---------------------------------------------------------

    def risk_level(self, score: float):

        if score >= 85:
            return "Very Low Risk"

        elif score >= 70:
            return "Low Risk"

        elif score >= 50:
            return "Moderate Risk"

        elif score >= 30:
            return "High Risk"

        return "Critical Risk"

    # ---------------------------------------------------------

    def analyze(self, user_id: int):

        features = self.get_features(user_id)

        prediction = self.predictor.predict(user_id)

        score = self.calculate_score(features)

        return {

            "user_id": int(user_id),

            "financial_health_score": float(score),

            "risk_level": self.risk_level(score),

            "prediction": prediction["prediction"],

            "confidence": float(prediction["confidence"]),

            "summary": {

                "income": float(round(features["income"], 2)),

                "expense": float(round(features["expense"], 2)),

                "savings": float(round(features["savings"], 2)),

                "savings_rate": float(
                    round(features["savings_rate"] * 100, 2)
                )

            }

        }


# ---------------------------------------------------------

if __name__ == "__main__":

    analyzer = RiskAnalyzer()

    result = analyzer.analyze(1)

    print()

    print(result)