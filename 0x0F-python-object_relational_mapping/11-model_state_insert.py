#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database
hbtn_0e_6_usa
"""
from typing import final
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
import sys

from model_state import Base, State

if __name__ == "__main__":
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
        *sys.argv[1:])
    engine = create_engine(DATABASE_URL)
    session = sessionmaker(bind=engine)()
    record = State(name="Louisiana")
    session.add(record)

    try:
        session.flush()
        session.refresh(record)
        if record is not None:
            print("{}".format(record.id))
    except Exception:
        session.rollback()
    finally:
        session.commit()
