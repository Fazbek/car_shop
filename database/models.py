from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, autoincrement=True, primary_key=True)
    model_of_car = Column(String, default="Select your type of cars", nullable=False)  # BMW,Ferrari
    type = Column(String, nullable=False)  # Sportcar, default car ...
    datetime = Column(DateTime, default=datetime.utcnow)

    category = relationship("CategoryCars", back_populates="cars")


class CategoryCars(Base):
    __tablename__ = "category_cars"
    id_detail = Column(Integer, autoincrement=True, primary_key=True)  # ID
    colour = Column(String, nullable=False)  # White , Pink ...
    strength_of_car = Column(Integer, nullable=False)  # horsepower
    date_of_issue = Column(Integer, nullable=False)
    amount_of_cars = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    datetime = Column(DateTime, default=datetime.utcnow)

    cars = relationship("Cars", back_populates="category")
