#!/usr/bin/python3
"""
Contains the class definition of a State that inherits from
declarative_base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class implementation of the State object"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', cascade='all, delete, delete-orphan', backref='state')
