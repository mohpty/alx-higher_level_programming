#!/usr/bin/python3
"""
    Start Link class to table in database
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    adr = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(adr.format(argv[1],
                                      argv[2],
                                      argv[3],
                                      pool_pre_ping=True))
    Base.metadata.create_all(engine)
