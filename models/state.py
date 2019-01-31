#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    __tablename__: the name of the table created in the database
        name: input name
    """
    __tablename__ = 'states'
    # for DB Storage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")

    else:
    # for FileStorage
        name = ""

        @property
        def cities(self):
            """"Returns the list of City instances with state_id equal to the
            current State.id"""
            ls = []
            for value in storage.all("City").values():
                if value.state_id == self.id:
                    ls.append(value)
                    # Check if cities setting does not take
            return ls
