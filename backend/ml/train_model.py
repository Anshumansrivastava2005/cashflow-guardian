import os
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# -----------------------------
# File Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "transactions.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "app",
    "ml",
    "model.pkl"
)

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(DATASET_PATH)

# -----------------------------
# Convert Type
# -----------------------------

df["type"] = df["type"].map({
    "Income": 1,
    "Expense": 0
})

# -----------------------------
# Features
# -----------------------------

X = df[["type"]]

y = df["amount"]

# -----------------------------
# Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train
# -----------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------

predictions = model.predict(X_test)

mse = mean_squared_error(
    y_test,
    predictions
)

print(f"\nModel Trained Successfully")
print(f"MSE : {mse:.2f}")

# -----------------------------
# Save Model
# -----------------------------

joblib.dump(model, MODEL_PATH)

print("\nModel Saved Successfully")
print(f"Saved at: {MODEL_PATH}")