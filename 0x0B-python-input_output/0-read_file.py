#!/usr/bin/python3
""" A module that provide a function that reads a file content """


def read_file(filename=""):
    """
        reads the content of file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
