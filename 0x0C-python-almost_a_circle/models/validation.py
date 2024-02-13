#!/usr/bin/python3
"""
    This module contains all the methods
    for validating user input
"""


def isInt(attr, value):
    '''check if the value passed is int'''

    msg = attr + ' must be an integer'
    if type(value) is not int:
        raise TypeError(msg)
    else:
        return True


def biggerThanZero(attr, value):
    '''
    check if the value passed is
    greater than zero'''

    msg = attr + ' must > 0'
    if value <= 0:
        raise ValueError(msg)
    else:
        return True


def biggerThanOrEqualZero(attr, value):
    '''
    check if the value passed is
    greater than or equal to zero'''

    msg = attr + ' must be >= 0'
    if value < 0:
        raise ValueError(msg)
    else:
        return True
