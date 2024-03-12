#!/usr/bin/python3
<<<<<<< HEAD
"""Module for print_square"""

import numpy

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        riturn m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
=======
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
