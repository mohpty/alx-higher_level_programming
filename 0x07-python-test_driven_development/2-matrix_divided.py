#!/usr/bin/python3
"""Module for matrix_div"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: List of lists of integers or floats.
        div: The divisor, a number (integer or float).

    Returns:
        A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(element, (int, float)) for row in matrix for element in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
