#!/usr/bin/python3
"""
    A module that provides a function that appends to existing textfile
"""


def append_write(filename='', text=''):
    """function that appends to an existing file, if it doesn't exist it will create it"""
    with open(filename, mode='a+', encoding='utf-8') as f:
        return f.write(text)

