#!/usr/bin/python3
"""This module contains the definition of the class square"""
from . import rectangle as rect


class Square(rect.Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size // 2, size // 2, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.height * self.width)
