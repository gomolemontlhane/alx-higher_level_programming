#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Creating engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the state with id 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Updating the state name if state exists
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    # Closing session
    session.close()

