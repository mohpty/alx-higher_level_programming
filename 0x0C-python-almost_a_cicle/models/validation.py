#!/usr/bin/python3

def isInt(attr, value):
    msg = attr + ' must be an integer'
    if type(value) is not int:
        raise TypeError(msg)
    else:
        return True

def biggerThanZero(attr, value):
    msg = attr + ' must > 0'
    if value <= 0:
        raise ValueError(msg)
    else:
        return True

def biggerThanOrEqualZero(attr, value):
    msg = attr + ' must be >= 0'
    if value < 0:
        raise ValueError(msg)
    else:
        return True
