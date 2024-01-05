#!/usr/bin/python3
""" define a rectangle"""


class Rectangle:
    """rectangle class."""

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width: Width of the rectangle.
            height: height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer
            ValueError: TypeError: If width or height less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width of rectangle

        Args:
            value (int): The new width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter Rectangle height.

        Args:
            value (int): The new height.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
