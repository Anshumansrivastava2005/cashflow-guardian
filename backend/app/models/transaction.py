from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    type = Column(String, nullable=False)

    category = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    description = Column(String, nullable=True)

    date = Column(String, nullable=False)