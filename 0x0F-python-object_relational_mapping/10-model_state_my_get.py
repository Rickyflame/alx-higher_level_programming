#!/usr/bin/python3
"""
A script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
import sys

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(*sys.argv[1:-1]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    record = session.query(State).order_by(State.id.asc()).filter(
        State.name == sys.argv[-1]).first()
    if record is not None:
        print(record.id)
    else:
        print("Not found")
