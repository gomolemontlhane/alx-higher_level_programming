#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create cursor object
    cursor = db.cursor()

    # Prepare SQL query using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute SQL query with user input as parameters
        cursor.execute(query, (state_name,))
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        # Display results
        for row in results:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close database connection
        db.close()

