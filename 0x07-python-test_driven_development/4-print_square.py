#!/usr/bin/python3
<<<<<<< HEAD
"""Module for print_square"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size: is size length of the sqiare

    Raises:
        TypeError: if size not an integer
        ValueError: if size less than 0
    """

=======
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

<<<<<<< HEAD
    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
=======
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
