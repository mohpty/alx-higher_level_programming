#!/usr/bin/python3
""" define class rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width: Width of the rectangle.
            height: height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer
            ValueError: TypeError: If width or height less than 0
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width of rectangle

        Args:
            value (int): The new width.

        Raises:
            TaypeError: If value is not an integer.
            ValueError: If value is less than 0.
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
        """ setter height

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol_line = str(self.print_symbol) * self.__width
            return "\n".join(symbol_line for i in range(self.__height))

    def __repr__(self):
        """Return a representation of the rectangle using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when instance of Rectangle deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
