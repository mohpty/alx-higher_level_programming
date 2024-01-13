#!/usr/bin/python3
"""This module contains the definition of the class rectangle"""
from . import base
from . import validation as v

class Rectangle(base.Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        v.isInt('width', width)
        v.isInt('height', height)
        v.isInt('x', x)
        v.isInt('y', y)

        v.biggerThanZero('height', height)
        v.biggerThanZero('width', width)

        v.biggerThanOrEqualZero('x', x)
        v.biggerThanOrEqualZero('y', y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        v.isInt('width', value)
        v.biggerThanZero('width', value)

        self.__width = value

    @height.setter
    def height(self, value):
        v.isInt('height', value)
        v.biggerThanZero('height', value)

        self.__height = value

    @x.setter
    def x(self, value):
        v.isInt('x', value)
        v.biggerThanOrEqualZero('x', value)

        self.__x = value

    @y.setter
    def y(self, value):
        v.isInt('y', value)
        v.biggerThanOrEqualZero('y', value)

        self.__y = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """
        displays the area of the rectangle
        using # symbols
        """
        for i in range(self.height):
            print('#' * self.width)
