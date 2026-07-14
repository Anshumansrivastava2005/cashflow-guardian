from fastapi import FastAPI

from app.database.database import Base, engine

from app.models.user import User
from app.models.transaction import Transaction

from app.routers.user import router as user_router
from app.routers.transaction import router as transaction_router
from app.routers.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CashFlow Guardian API",
    version="1.0.0",
    description="AI-Driven Cash Flow Prediction & Risk Flagging System"
)

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": "CashFlow Guardian API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }