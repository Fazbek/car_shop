from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Cars(Base):
    __tablename__ = "car"
    id = Column(Integer, autoincrement=True, primary_key=True)
    category_id = Column(Integer, ForeignKey('category_cars.id_detail'))
    model_of_car = Column(String, default="Select your type of cars", nullable=False)  # BMW,Ferrari
    type_of_car = Column(String, nullable=False)  # Sportcar, default car ...

    category = relationship("CategoryCars", back_populates="cars")


class CategoryCars(Base):
    __tablename__ = "category_cars"
    id_detail = Column(Integer, autoincrement=True, primary_key=True)  # ID
    colour = Column(String, nullable=False)  # White , Pink ...
    strength_of_car = Column(Integer, nullable=False)  # horsepower
    date_of_issue = Column(Integer, nullable=False)
    amount_of_cars = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

    cars = relationship("Cars", back_populates="category")
