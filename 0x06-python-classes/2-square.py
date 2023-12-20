#!/usr/bin/python3
"""Square class"""


class Square:
    """ Represents a square with a side length """

    def __init__(self, size=0):
        """ initializ square with the given side length

        Args:
            size: side length of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
