"""
sim_transaction.py

SQLAlchemy model used for storing AI generated
transactions. These transactions are completely
separate from real user transactions.
"""

from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.database.database import Base


class SimTransaction(Base):
    __tablename__ = "sim_transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    sim_user_id = Column(
        Integer,
        ForeignKey("sim_users.id"),
        nullable=False
    )

    type = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    description = Column(
        String
    )

    date = Column(
        String,
        nullable=False
    )

    payment_method = Column(
        String,
        default="UPI"
    )

    merchant = Column(
        String,
        default="Unknown"
    )

    recurring = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "SimUser",
        back_populates="transactions"
    )