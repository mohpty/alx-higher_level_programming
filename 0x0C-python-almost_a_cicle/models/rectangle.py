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

    def update(self, *args, **kwargs):
        """
        update the args
        using no-keyword argument
        """
        if len(args) > 0:
            try:
                if args[0]:
                    v.isInt('id', args[0])
                    self.id = args[0]
                if args[1]:
                    self.width(args[1])
                if args[2]:
                    self.height(args[2])
                if args[3]:
                    self.x(args[3])
                if args[4]:
                    self.y(args[4])
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                v.isInt('id', kwargs['id'])
                self.id = kwargs['id']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


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
        print('\n' * self.y,end='')
        for i in range(self.height):
            print(' ' * self.x, '#' * self.width, sep='')

    def to_dictionary(self):
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

