#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine import create_engine
import sys

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(*sys.argv[1:])
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
