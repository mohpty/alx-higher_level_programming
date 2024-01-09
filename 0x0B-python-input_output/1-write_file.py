#!/usr/bin/python3
"""A module that provides a function to write to a file"""


def write_file(filename="", text=''):
    """
        Writes a text to a file,
            if it exists it will overrite the content
            if not it will create the file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    f.close()
