#!/usr/bin/python3
"""Square class"""


class Square:
    """ Represents a square with a side length """

    def __init__(self, size=0):
        """ initializ square with the given side length

        Args:
            size: side length of square
        """
        self.__size = size

    @property
    def size(self):
        """
        getter property for side of square.

        Raises:
            TypeError: if size not integer.
            ValueError: if size less 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area

        Returns:
            The current square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints square with character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * (self.__size))
