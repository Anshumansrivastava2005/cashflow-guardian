from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

# Import ALL models so SQLAlchemy creates their tables
from app.models.user import User
from app.models.transaction import Transaction
from app.models.sim_user import SimUser
from app.models.sim_transaction import SimTransaction

# Routers
from app.routers.user import router as user_router
from app.routers.transaction import router as transaction_router
from app.routers.dashboard import router as dashboard_router
from app.routers.ai import router as ai_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CashFlow Guardian API",
    version="1.0.0",
    description="AI-Driven Cash Flow Prediction & Risk Flagging System",
)

# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Register Routers
# ---------------------------------------------------------

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(dashboard_router)
app.include_router(ai_router)

# ---------------------------------------------------------
# Root
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Welcome to CashFlow Guardian API 🚀",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "CashFlow Guardian API",
        "version": "1.0.0",
    }