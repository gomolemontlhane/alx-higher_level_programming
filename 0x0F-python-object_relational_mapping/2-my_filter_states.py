#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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

    # Execute query
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))

    # Fetch all rows and print
    for row in cur.fetchall():
        print(row)

    # Close cursor and database
    cur.close()
    db.close()

