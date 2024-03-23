#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creating engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", "hbtn_0e_6_usa"),
                           pool_pre_ping=True)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying
    states_with_a = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    # Displaying result
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Closing session
    session.close()
