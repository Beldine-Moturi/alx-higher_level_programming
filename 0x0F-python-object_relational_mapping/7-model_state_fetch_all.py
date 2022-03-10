#!/usr/bin/python3
"""Lists all rows of a table in a database using SQLAlchemy"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys


if __name__ == "__main__":
    db_info = sys.argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        db_info[0],
        db_info[1],
        db_info[2]
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id)
    for state in all_states:
        print("{}: {}".format(state.id, state.name))

    session.close()
