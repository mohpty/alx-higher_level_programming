#!/usr/bin/python3
""" define magicclass """

import math


class MagicClass:
    """ represent circale """

    def __init__(self, radius=0):
        """ init a magic class

        Args:
            radius: radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        return the area.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference of magic class.
        """
        return 2 * math.pi * self.__radius
