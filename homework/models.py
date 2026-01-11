from sqlalchemy import Column, String, Integer
from database import Base
import os

class Recipe(Base):
    __tablename__ = 'Recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    views = Column(Integer, default=0)
    time_to_cook = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
