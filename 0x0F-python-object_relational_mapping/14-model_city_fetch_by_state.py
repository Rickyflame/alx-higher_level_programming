#!/usr/bin/python3
"""
A script that prints all City objects from a db
"""
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine import create_engine
import sys

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    State.cities = relationship('City', back_populates='state')
    session = sessionmaker(bind=engine)()
    records = session.query(City).order_by(City.id.asc())
    for record in records:
        print("{}: ({}) {}".format(record.state.name, record.id, record.name))
