#!/usr/bin/python3
"""Performing basic database connection and executing a simple sql script
that list all states starting with uppercase N
USAGE: ./0-select_states.py [username] [password] [database]"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2],
                         database=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in c.fetchall():
        if state[1] == argv[4]:
            print(state)
