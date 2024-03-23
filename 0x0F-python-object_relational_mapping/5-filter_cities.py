#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa that match a state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute queries
    cur = db.cursor()

    # Execute query to fetch cities of the specified state
    cur.execute("""
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch the result
    result = cur.fetchone()[0]

    # Print the result or 'Not found' if no cities found for the state
    print(result if result else 'Not found')

    # Close cursor and database
    cur.close()
    db.close()