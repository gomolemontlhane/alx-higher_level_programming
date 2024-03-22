#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create cursor object
    cursor = db.cursor()

    # Prepare SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    try:
        # Execute SQL query
        cursor.execute(query)
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

