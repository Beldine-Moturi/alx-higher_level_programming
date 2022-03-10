#!/usr/bin/python3
"""Uses sqlalchemy to coonect to a database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Iteger
import sys


Base = declarative_base()


class State(Base):
    """The class used to define the states table"""

    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
