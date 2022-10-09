#!/usr/bin/python3
"""Contains the class definition of a City"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """The implementation of the City class"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
