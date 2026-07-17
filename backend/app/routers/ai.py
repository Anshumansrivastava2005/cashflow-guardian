"""
AI Router

Exposes AI services:

- Simulate users
- Train model
- Predict risk
- Financial advice
- Risk analysis
"""

from fastapi import APIRouter, HTTPException

from app.ai.simulator import FinancialSimulator
from app.ai.trainer import ModelTrainer
from app.ai.predictor import Predictor
from app.ai.advisor import FinancialAdvisor
from app.ai.risk import RiskAnalyzer

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"]
)


# ---------------------------------------------------------
# Initialize AI modules
# ---------------------------------------------------------

simulator = FinancialSimulator()

trainer = ModelTrainer()

predictor = Predictor()

advisor = FinancialAdvisor()

risk = RiskAnalyzer()


# ---------------------------------------------------------
# Simulate Dataset
# ---------------------------------------------------------

@router.post("/simulate")
def simulate_users(users: int = 100):

    try:

        simulator.simulate(users)

        return {

            "status": "success",

            "message": f"{users} users generated successfully."

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ---------------------------------------------------------
# Train AI Model
# ---------------------------------------------------------

@router.post("/train")
def train_model():

    try:

        trainer.train()

        return {

            "status": "success",

            "message": "AI model trained successfully."

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ---------------------------------------------------------
# Predict User
# ---------------------------------------------------------

@router.get("/predict/{user_id}")
def predict(user_id: int):

    try:

        result = predictor.predict(user_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# ---------------------------------------------------------
# Advice
# ---------------------------------------------------------

@router.get("/advice/{user_id}")
def advice(user_id: int):

    try:

        result = advisor.advise(user_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    
    # ---------------------------------------------------------
# Risk Analysis
# ---------------------------------------------------------

@router.get("/risk/{user_id}")
def analyze_risk(user_id: int):

    try:

        result = risk.analyze(user_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

@router.get("/statistics")
def statistics():

    try:

        result = simulator.statistics()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ---------------------------------------------------------
# Reset Simulation Database
# ---------------------------------------------------------

@router.delete("/reset")
def reset_database():

    try:

        simulator.reset_database()

        return {

            "status": "success",

            "message": "Simulation database reset successfully."

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@router.get("/health")
def health():

    return {

        "status": "online",

        "service": "CashFlow Guardian AI",

        "modules": {

            "simulator": True,

            "trainer": True,

            "predictor": True,

            "advisor": True,

            "risk": True

        }

    }


# ---------------------------------------------------------
# Root
# ---------------------------------------------------------

@router.get("/")
def root():

    return {

        "message": "CashFlow Guardian AI API",

        "available_endpoints": [

            "/ai/simulate",

            "/ai/train",

            "/ai/predict/{user_id}",

            "/ai/advice/{user_id}",

            "/ai/risk/{user_id}",

            "/ai/statistics",

            "/ai/reset",

            "/ai/health"

        ]

    }