#!/usr/bin/python3
"""
A script that changes the name of a State object from a database
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
    record = session.query(State).filter_by(id=2).first()
    record.name = 'New Mexico'
    try:
        session.flush()
        session.refresh(record)
    except Exception:
        session.rollback()
    finally:
        session.commit()
