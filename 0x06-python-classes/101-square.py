#!/usr/bin/python3


class Square:
    """ Represents a square with a side length """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializ square with the given side length

        Args:
            size: side length of square
            position: position of the square as a tuple.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter for position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter position attribue

        Args:
            value or tuple: The new position of the square.

        Raises:
            TypeError:  position must be a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(k, int) for k in value) or
                not all(k >= 0 for k in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def __str__(self):
        if self.size == 0:
            return ""

        sq_row = [
                " " * self.__position[0] + "#" * self.__size
                for i in range(self.__size)
        ]
        return "\n".join(sq_row)
