"""
sim_user.py

SQLAlchemy model used for storing AI-generated users.
These users are completely separate from real users.
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.database.database import Base


class SimUser(Base):
    __tablename__ = "sim_users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    gender = Column(
        String,
        nullable=False
    )

    city = Column(
        String,
        nullable=False
    )

    occupation = Column(
        String,
        nullable=False
    )

    monthly_income = Column(
        Float,
        nullable=False
    )

    lifestyle = Column(
        String,
        nullable=False
    )

    risk_profile = Column(
        String,
        default="Medium"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    transactions = relationship(
        "SimTransaction",
        back_populates="user",
        cascade="all, delete-orphan"
    )