#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database,
                         charset="utf8")

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    query_rows = cursor.fetchall()

    # Print results
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
    