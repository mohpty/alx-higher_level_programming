#!/usr/bin/python3
"""This module contains the definition of the class square"""
from . import rectangle as rect
from . import validation as v


class Square(rect.Rectangle):
    """
        Subclass of the rectangle,
        basically a rectangle with the same
        values for the height and width
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        v.isInt('width', value)
        v.biggerThanZero('width', value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the attribute values"""
        if len(args) > 0:
            try:
                if args[0]:
                    v.isInt('id', args[0])
                    self.id = args[0]
                if args[1]:
                    self.width = args[1]
                    self.height = args[1]
                if args[2]:
                    self.x = args[2]
                if args[3]:
                    self.y = args[3]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']

            if 'size' in kwargs:
                self.height = kwargs['size']
                self.width = kwargs['size']

            if 'x' in kwargs:
                self.x = kwargs['x']

            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Converts the object to a dictionary"""
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        '''return a readable string of the instance'''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)
