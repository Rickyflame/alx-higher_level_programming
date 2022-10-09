#!/usr/bin/python3
"""
Contains the class definition of a state that inherits from declarative_base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class implementation of the State object"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
