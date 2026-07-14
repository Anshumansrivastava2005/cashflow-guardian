import os
import joblib
import numpy as np
import pandas as pd

from xgboost import XGBRegressor

MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "model.pkl"
)


class CashFlowTrainer:

    def __init__(self):
        self.model = XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42
        )

    def train(self, dataframe: pd.DataFrame):

        if dataframe.empty:
            raise Exception("No data available for training.")

        X = dataframe.drop(columns=["target"])

        y = dataframe["target"]

        self.model.fit(X, y)

        joblib.dump(
            self.model,
            MODEL_PATH
        )

        return {
            "message": "Model Trained Successfully",
            "samples": len(dataframe),
            "model_path": MODEL_PATH
        }