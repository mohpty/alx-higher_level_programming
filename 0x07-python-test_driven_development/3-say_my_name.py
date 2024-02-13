#!/usr/bin/python3
<<<<<<< HEAD
"""Module for say_my_name"""

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the first and last name.

    Args:
        first_name: The first name (required).
        last_name: The last name (optional).

    Raises:
        TypeError: If either first_name or last_name is not a string.

    """

=======
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
<<<<<<< HEAD

    print(f"My name is {first_name} {last_name}")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
=======
    print("My name is {} {}".format(first_name, last_name))
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
