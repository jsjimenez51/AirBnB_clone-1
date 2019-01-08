#!/usr/bin/python3
"""
Module defines  DB storage
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """
    Defines DBstorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        initializes the db storage engine
        """

        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysl+mysqldb://{}:{}@{}/{}'.format(user,\
                                      pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_MYSQL_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
