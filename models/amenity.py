#!/usr/bin/python3
""" State Module for HBNB proje"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

HBNB_STORAGE_TYPE = os.environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if HBNB_STORAGE_TYPE == "db":
        place_amenities = relationship(
            "Place",
            secondary=place_amenity,
            back_populates="amenities",
            viewonly=False,
        )