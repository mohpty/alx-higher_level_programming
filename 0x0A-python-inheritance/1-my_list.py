#!/usr/bin/python3
"""
contains MyList class declaration
"""


class MyList(list):
    """ subclass of the list class """
    def __init__(self):
        """Initialization of the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
