#!/usr/bin/python3
"""Filter row that contain a certain name"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).all()
    if state:
        print(state[0].id)
    else:
        print("Not found")

    session.close()
