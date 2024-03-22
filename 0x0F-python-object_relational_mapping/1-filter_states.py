#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of the database hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")

    # Create cursor object
    cur = conn.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print query results
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()

