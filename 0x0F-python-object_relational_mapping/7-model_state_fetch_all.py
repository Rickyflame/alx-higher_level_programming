#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    records = session.query(State).all()
    for record in records:
        print("{}: {}".format(record.id, record.name))
