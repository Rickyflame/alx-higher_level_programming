#!/usr/bin/python3
"""
A script that deletes all State objects with name containing letter a
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
import sys

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    a_records = session.query(State).filter(
        State.name.contains(r"%a%")).delete(synchronize_session=False)
    session.commit()
