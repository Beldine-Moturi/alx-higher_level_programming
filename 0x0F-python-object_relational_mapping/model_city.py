#!/usr/bin/python3
"""defines the class city that represents the cities table
in a database"""

from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey


class City(Base):
    """Represents the table `cities` in a database"""

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
