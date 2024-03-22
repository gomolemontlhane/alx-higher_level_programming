#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a' from
the database hbtn_0e_6_usa
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

    # Querying states containing letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Deleting states
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Closing session
    session.close()

