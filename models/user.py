#!/usr/bin/python3
"""This module defines a User class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """This class defines a user by various attributes
    email: email address
    password: login password
    first_name: user's first name
    last_name: user's last name
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
