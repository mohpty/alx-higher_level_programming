#!/usr/bin/python3
"""Performing basic database connection and executing a simple sql script
USAGE: ./0-select_states.py [username] [password] [database]"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for state in cursor.fetchall():
        print(state)
