#!/usr/bin/python3
<<<<<<< HEAD
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

=======
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

<<<<<<< HEAD
    if not isinstance(div, (int, float)):
=======
    if not isinstance(div, int) and not isinstance(div, float):
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

<<<<<<< HEAD
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
=======
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
