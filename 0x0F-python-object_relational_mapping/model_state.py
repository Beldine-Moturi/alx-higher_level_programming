#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Iteger

Base = declarative_base()


class State(Base):
    """The class used to define the states table"""

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
