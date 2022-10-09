#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
import sys

from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:])
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    records = session.query(State).order_by(State.id.asc()).all()
    for record in records:
        print("{}: {}".format(record.id, record.name))
        for city in record.cities:
            print("\t{}: {}".format(city.id, city.name))
