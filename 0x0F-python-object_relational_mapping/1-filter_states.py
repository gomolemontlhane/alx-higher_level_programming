#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and print
    for row in cur.fetchall():
        print(row)

    # Close cursor and database
    cur.close()
    db.close()