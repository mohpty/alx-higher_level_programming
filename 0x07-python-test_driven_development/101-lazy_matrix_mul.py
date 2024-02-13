#!/usr/bin/python3
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
