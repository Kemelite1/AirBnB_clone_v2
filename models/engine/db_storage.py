#!/usr/bin/python3
"""Database storage for HBNB"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """Manages the database storage for HBNB models"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates a new instance of DBStorage"""
        hbnb_user = os.getenv("HBNB_MYSQL_USER")
        hbnb_pwd = os.getenv("HBNB_MYSQL_PWD")
        hbnb_host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        hbnb_db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(hbnb_user, hbnb_pwd, hbnb_db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of __object"""
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
                query = self.__session.query(cls)
                for element in query:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    dictionary[key] = element

        else:
            lists = [User, State, City, Place, Review, Amenity]
            for c in lists:
                query = self.__session.query(c)
                for element in query:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    dictionary[key] = element
        return dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an element from the current database table"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates table and current database - configuration"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self, expire_on_commit=False)
        self.__session = scoped_session(session)

