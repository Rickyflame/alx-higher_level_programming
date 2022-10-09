#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
import sys

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:])
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    results = session.query(City).join(State).order_by(City.id.asc())
    for city in results:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
