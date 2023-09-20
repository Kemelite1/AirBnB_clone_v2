#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.place import place

class City(BaseModel, Base):
    """
    The city class, contains state ID and name

    Attributes:
    state_id: the state id
    name: input name
    """

    __table__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    places = relationship("place", backref="cities", cascade="all, delete")
