#!/usr/bin/python3
"""Performing basic database connection and executing a simple sql script
that list the state that matches the input
USAGE: ./0-select_states.py [username] [password] [database] [state name]"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2],
                         database=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    for city in c.fetchall():
        print(city)
    c.close()
    db.close()
