from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from .db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True)

    email = Column(String, unique=True)

    password = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    expenses = relationship(
        "Expense",
        back_populates="owner"
    )


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    amount = Column(Float)

    category = Column(String)

    description = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    owner = relationship(
        "User",
        back_populates="expenses"
    )