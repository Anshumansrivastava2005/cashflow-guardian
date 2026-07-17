"""
trainer.py

Trains the CashFlow Guardian AI model.
"""

from pathlib import Path
import joblib

from sklearn.ensemble import RandomForestClassifier

from app.ai.feature_engine import FeatureEngine


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent.parent / "ml_models"

MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "cashflow_guardian.pkl"


class ModelTrainer:

    def __init__(self):

        self.feature_engine = FeatureEngine()

    # -------------------------------------------------

    def prepare_data(self):

        df = self.feature_engine.build_dataset()

        df["risk"] = (
            df["savings_rate"] < 0.20
        ).astype(int)

        X = df.drop(
            columns=[
                "user_id",
                "risk"
            ]
        )

        y = df["risk"]

        return X, y

    # -------------------------------------------------

    def train(self):

        X, y = self.prepare_data()

        model = RandomForestClassifier(

            n_estimators=200,

            random_state=42

        )

        model.fit(X, y)

        joblib.dump(

            model,

            MODEL_PATH

        )

        print()

        print("=" * 60)

        print("AI Model Trained Successfully")

        print("=" * 60)

        print()

        print("Model Saved To:")

        print(MODEL_PATH)

        print()

        return model


# -------------------------------------------------

if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.train()