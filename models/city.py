#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        __tablename__: the name of the table created in the database
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('state.id'))
