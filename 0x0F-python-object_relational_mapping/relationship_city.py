#!/usr/bin/python3
"""defines the class city that represents the cities table
in a database"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents the table `cities` in a database"""

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
