# SQL Introduction

This repository contains SQL scripts for basic database management tasks. Each script is designed to perform a specific action on a MySQL database.

## Author

Gomolemo Ntlhane

## Table of Contents

- [List of Scripts](#list-of-scripts)
- [Usage](#usage)
- [License](#license)

## List of Scripts

1. **0-list_databases.sql**: Lists all databases on the MySQL server.
2. **1-create_database_if_missing.sql**: Creates a database if it doesn't already exist.
3. **2-remove_database.sql**: Deletes a database if it exists.
4. **3-list_tables.sql**: Lists all tables in a specified database.
5. **4-first_table.sql**: Creates a table called first_table.
6. **5-full_table.sql**: Displays the full description of the first_table.
7. **6-list_values.sql**: Lists all rows of the first_table.
8. **7-insert_value.sql**: Inserts a new row into the first_table.
9. **8-count_89.sql**: Counts the number of records with id = 89 in the first_table.
10. **9-full_creation.sql**: Creates a table called second_table and adds multiple rows.
11. **10-top_score.sql**: Lists all records from the second_table ordered by score.
12. **11-best_score.sql**: Lists records with a score >= 10 from the second_table ordered by score.
13. **12-no_cheating.sql**: Updates Bob's score to 10 without using Bob's id.
14. **13-change_class.sql**: Removes all records with a score <= 5 from the second_table.
15. **14-average.sql**: Computes the average score from the second_table.
16. **15-groups.sql**: Lists the number of records for each score from the second_table.
17. **16-no_link.sql**: Lists all records with names from the second_table ordered by score.

## Usage

To use these scripts, simply execute them using a MySQL client such as the MySQL command-line tool or MySQL Workbench. Make sure to provide the necessary credentials and specify the database name if required.

Example:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
## MySQL Installation

To run these scripts, you need to have MySQL installed on your system. If you haven't installed MySQL yet, follow these steps:

1. Update package index:

```bash
sudo apt update
```
1. Install MySQL server:

```bash
sudo apt install mysql-server
```
1. Start MySQL service:

```bash
sudo service mysql start
```
# MySQL Server Connection

## Connecting to MySQL Server on Ubuntu 20.04

To connect to the MySQL server on Ubuntu 20.04 using the command line, follow these steps:

1. Open your terminal.

2. Use the following command to connect to the MySQL server:
    ```bash
    mysql -u username -p -h localhost
    ```
    Replace `username` with your MySQL username.

    If you're connecting to a remote MySQL server, replace `localhost` with the IP address or hostname of the server.

3. After running the command, you'll be prompted to enter your MySQL password.

4. Once you've entered the correct password, you'll be connected to the MySQL server.

### Example:

```bash
mysql -u root -p -h localhost

