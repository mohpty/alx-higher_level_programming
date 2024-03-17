#!/usr/bin/python3
"""Performing basic database connection and executing a simple sql script
that list the cities of a state that matches the input
USAGE: ./0-select_states.py [username] [password] [database] [state name]"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2],
                         database=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states ON \
            cities.state_id = states.id WHERE states.name = %s", (argv[4],))
    cities = c.fetchall()
    for i in range(len(cities)):
        print(cities[i][0], end='')
        if i != len(cities) - 1:
            print(end=', ')
    print()
