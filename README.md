# ALX Higher Level Programming

## Overview

This repository contains comprehensive higher-level programming projects covering Python fundamentals, object-oriented programming, database management (SQL), and JavaScript. The projects progress from basic syntax and control flow through advanced concepts including data structures, exception handling, OOP principles, network programming, and web technologies.

## Repository Structure

The repository is organized into 22 progressive projects:

### Core Projects Summary

This repository covers:

- **Python Basics (0x00-0x02)** - Hello world, conditionals, loops, and module imports
- **Data Structures (0x03-0x04)** - Lists, tuples, dictionaries, and set operations
- **Exception Handling (0x05)** - Error handling and custom exceptions
- **Object-Oriented Programming (0x06-0x0A)** - Classes, inheritance, and polymorphism
- **File I/O & Serialization (0x0B)** - Reading, writing, and JSON handling
- **Python Projects (0x0C)** - Practical applications: Almost a Circle project
- **Database Programming (0x0D-0x0F)** - SQL basics, advanced queries, and ORM concepts
- **Network Programming (0x10-0x11)** - HTTP requests, URL handling, and socket programming
- **JavaScript Basics (0x12-0x15)** - JavaScript syntax, DOM manipulation, and jQuery

## Detailed Project Breakdown

### Shell Scripting & Basics

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| Hello, World | 0x00-python-hello_world | Print statements, Python interpreter | Beginner |
| If/Else, Loops | 0x01-python-if_else_loops_fu... | Conditionals, loops (for/while) | Beginner |
| Import & Modules | 0x02-python-import_modules | Module imports, code organization | Beginner |

### Data Structures & Algorithms

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| Data Structures | 0x03-python-data_structures | Lists, tuples, basic algorithms | Intermediate |
| More Data Structures | 0x04-python-more_data_stru... | Dictionaries, sets, advanced operations | Intermediate |
| Exceptions | 0x05-python-exceptions | Exception handling, try/except/finally | Intermediate |

### Object-Oriented Programming

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| Classes | 0x06-python-classes | Basic OOP, class definition, attributes | Intermediate |
| Test Driven Development | 0x07-python-test_driven_dev... | Unit testing, docstring testing | Intermediate |
| More Classes | 0x08-python-more_classes | Class methods, static methods, properties | Intermediate |
| Everything is Object | 0x09-python-everything_is_o... | Object model, metaclasses, built-in types | Advanced |
| Inheritance | 0x0A-python-inheritance | Inheritance, super(), MRO | Advanced |

### Advanced Python

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| Input/Output | 0x0B-python-input_output | File operations, JSON serialization | Intermediate |
| Almost a Circle | 0x0C-python-almost_a_circle | Project: Rectangle/Square classes | Advanced |

### Database & SQL

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| SQL Introduction | 0x0D-SQL_introduction | Basic SQL (SELECT, INSERT, UPDATE) | Intermediate |
| SQL More Queries | 0x0E-SQL_more_queries | JOINs, subqueries, advanced queries | Intermediate |
| Python Object-Relational | 0x0F-python-object_relational... | ORM concepts, SQLAlchemy basics | Advanced |

### Network Programming

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| Network 0 | 0x10-python-network_0 | HTTP basics, urllib, requests | Intermediate |
| Network 1 | 0x11-python-network_1 | HTTP requests, headers, POST data | Intermediate |

### JavaScript & Web

| Project | Directory | Topics | Difficulty |
|---------|-----------|--------|------------|
| JavaScript Warm-up | 0x12-javascript-warm_up | JavaScript syntax, functions, variables | Beginner |
| JavaScript Objects/Scope | 0x13-javascript_objects_scop... | Objects, scope, closures, prototypes | Intermediate |
| JavaScript Web Scraping | 0x14-javascript-web_scraping | Node.js, file operations, parsing | Intermediate |
| JavaScript Web jQuery | 0x15-javascript-web_jquery | DOM manipulation, jQuery, AJAX | Intermediate |

## Technology Stack

### Languages
- **Python 3** (0x00-0x11) - Primary language for most projects
- **SQL** (0x0D-0x0F) - Database querying and management
- **JavaScript ES6+** (0x12-0x15) - Web scripting and DOM manipulation
- **Bash** - Shell scripting for automation

### Tools & Frameworks
- **Unit Testing** - Python unittest, doctest
- **Web Frameworks** - Basic HTTP handling
- **Database** - MySQL, SQLite
- **Web Technologies** - jQuery, DOM APIs
- **Package Managers** - pip for Python dependencies

## Learning Outcomes

Upon completing this repository, you will:

- ✓ Understand Python fundamentals and advanced OOP concepts
- ✓ Master control flow, data structures, and algorithms
- ✓ Write clean, maintainable code with proper testing
- ✓ Handle exceptions and implement error handling
- ✓ Work with files, JSON, and serialization
- ✓ Design and implement class hierarchies using inheritance
- ✓ Write and optimize SQL queries
- ✓ Understand network programming and HTTP protocols
- ✓ Develop basic JavaScript applications
- ✓ Manipulate the DOM using vanilla JavaScript and jQuery
- ✓ Implement test-driven development practices

## Installation & Setup

### Prerequisites
- Python 3.6+
- pip (Python package installer)
- Node.js (for JavaScript projects)
- SQL database (MySQL/SQLite)
- Text editor or IDE (VS Code, PyCharm)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/gomolemontlhane/alx-higher_level_programming.git
cd alx-higher_level_programming

# Navigate to a project
cd 0x00-python-hello_world

# Run a Python script
python3 0-hello.py

# Run SQL files
mysql -u root -p < 0x0D-SQL_introduction/0-list_databases.sql

# Run JavaScript files
node 0x12-javascript-warm_up/0-javascript.js
```

## Project Structure per Project

Each project directory typically contains:

```
0x##-project_name/
├── README.md                 # Project-specific documentation
├── task_0.py/js/sql         # Solution files for each task
├── task_1.py/js/sql
├── main.py                  # Test/driver files
├── tests/                   # Test files (if applicable)
└── ...
```

## Common Tasks & Examples

### Python Task Example (0x01-python-if_else_loops_fu...)

```python
#!/usr/bin/python3
"""Print positive, negative, or zero"""

number = int(input())

if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("{} is zero".format(number))
```

### SQL Task Example (0x0D-SQL_introduction)

```sql
-- List all databases
SHOW DATABASES;

-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- List all tables in a database
SHOW TABLES FROM database_name;
```

### JavaScript Task Example (0x12-javascript-warm_up)

```javascript
#!/usr/bin/node
// Print string multiple times

let args = process.argv.slice(2);
let string = args[0];
let times = parseInt(args[1]);

for (let i = 0; i < times; i++) {
    console.log(string);
}
```

## Key Concepts by Topic

### Python Fundamentals
- Data types: int, float, str, bool, list, dict, tuple, set
- Control flow: if/elif/else, for loops, while loops
- Functions: definition, parameters, return values, *args, **kwargs
- List comprehensions and generator expressions
- Lambda functions and functional programming

### OOP Principles
- Classes and objects
- Instance vs. class variables
- Methods: instance, class, and static methods
- Inheritance: single and multiple inheritance
- Polymorphism and method overriding
- Special methods: __init__, __str__, __repr__
- Properties and decorators
- Abstract base classes

### Database Concepts
- CRUD operations (Create, Read, Update, Delete)
- SQL JOINs: INNER, LEFT, RIGHT, FULL OUTER
- Subqueries and nested queries
- Aggregation functions: COUNT, SUM, AVG, MAX, MIN
- Grouping and filtering: GROUP BY, HAVING
- Indexes and query optimization

### Web & Network
- HTTP methods: GET, POST, PUT, DELETE
- Request headers and response codes
- URL encoding and query parameters
- JSON data format and serialization
- Socket programming basics
- Web scraping and parsing

## Resources & References

### Python Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### SQL Resources
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [SQL Queries Best Practices](https://sqlperformance.com/)

### JavaScript Resources
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [jQuery Documentation](https://api.jquery.com/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [ES6 Features](https://es6-features.org/)

### Testing & Best Practices
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)
- [Code Quality Guidelines](https://pep8.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

## Quick Reference: Directories

| Code | Project Name | Focus |
|------|--------------|-------|
| 0x00 | Python Hello World | Basics |
| 0x01 | If/Else, Loops | Control Flow |
| 0x02 | Import & Modules | Code Organization |
| 0x03 | Data Structures | Lists, Tuples |
| 0x04 | More Data Structures | Dicts, Sets |
| 0x05 | Exceptions | Error Handling |
| 0x06 | Classes | OOP Basics |
| 0x07 | Test Driven Dev | Unit Testing |
| 0x08 | More Classes | Advanced OOP |
| 0x09 | Everything is Object | Metaprogramming |
| 0x0A | Inheritance | OOP Hierarchy |
| 0x0B | Input/Output | File Handling |
| 0x0C | Almost a Circle | Project |
| 0x0D | SQL Introduction | Database Basics |
| 0x0E | SQL More Queries | Advanced SQL |
| 0x0F | Python Object-Relational | ORM |
| 0x10 | Network 0 | HTTP Basics |
| 0x11 | Network 1 | Network Programming |
| 0x12 | JavaScript Warm-up | JS Basics |
| 0x13 | JS Objects/Scope | Advanced JS |
| 0x14 | JS Web Scraping | Node.js |
| 0x15 | JS Web jQuery | DOM & jQuery |

## Troubleshooting Guide

### Python Issues
- **ModuleNotFoundError**: Ensure module is installed (`pip install module_name`)
- **Syntax Errors**: Check Python version (should be 3.6+)
- **Encoding Issues**: Add `# -*- coding: utf-8 -*-` at file start
- **Permission Denied**: Make script executable (`chmod +x script.py`)

### SQL Issues
- **Connection Refused**: Check MySQL service is running
- **Access Denied**: Verify username and password
- **Database Not Found**: Use correct database name or CREATE DATABASE
- **Syntax Error**: Check SQL syntax against MySQL documentation

### JavaScript Issues
- **Cannot Find Module**: Install package (`npm install package_name`)
- **ReferenceError**: Check variable scope and declaration
- **jQuery Not Found**: Ensure jQuery library is loaded
- **DOM Not Ready**: Use `$(document).ready()` before DOM access

## Contributing

This is an educational repository. If you find improvements or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request with description

## Status & Difficulty

- **Repository Status**: Active Learning Project
- **Overall Difficulty**: Beginner → Advanced
- **Est. Time to Complete**: 6-12 months
- **Prerequisite Knowledge**: Basic computer science concepts
- **Recommended Pace**: 1 project per week

## License

This educational repository is provided as-is for learning purposes.

---

**Last Updated**: 2025
**Total Projects**: 22
**Total Lines of Code**: 5000+
