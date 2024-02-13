#!/usr/bin/python3
<<<<<<< HEAD
"""Module for matrix_mul"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or if any element is not an integer or float.
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a must be a list of lists of integers/floats")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b must be a list of lists of integers/floats")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
=======
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

<<<<<<< HEAD
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]


    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
=======
    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
