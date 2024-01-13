#!/usr/bin/python3
"""This module contains the definition of the class square"""
from . import rectangle as rect
from . import validation as v

class Square(rect.Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        v.isInt('width', value)
        v.biggerThanZero('width', value)
        self.width = value
        self.height = value

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.height)
