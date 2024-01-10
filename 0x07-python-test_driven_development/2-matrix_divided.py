#!/usr/bin/python3
"""Contains matrix_divided function"""


def matrix_divided(matrix, div):
    typerrmsg = "matrix must be a matrix (list of lists) of integers/floats"
    for ls in matrix:
        if not isinstance(ls, list):
            raise TypeError(typerrmsg)
        for num in ls:
            if not (isinstance(num, int) or (isinstance(num, float))):
                raise TypeError(typerrmsg)

        if sum([len(i) for i in matrix]) / len(matrix) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if not (isinstance(div, int) or isinstance(div, float)):
            raise TypeError('div must be a number')

        if div == 0:
            raise ZeroDivisionError('division by zero')

        new = matrix[:]
        return [[round(i / div, 2) for i in x] for x in matrix]
