
2. **2-filter_states.py**: This Python script retrieves and filters states from a MySQL database based on user input.

```python
#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
                         db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve states based on user input
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print the state information
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

