#!/usr/bin/python3
"""Performing basic database connection and executing a simple sql script
USAGE: ./0-select_states.py [username] [password] [database]"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='127.0.0.1',
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM states')
        for i in cursor:
            print(i)
