#!/usr/bin/python3
<<<<<<< HEAD
"""Module for text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: string to printed

        Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in ".?:":
        text = (delimeter + "\n\n").join([line.strip(" ") for line in text.split(delimeter)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
=======
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
>>>>>>> e6e82de04bed8e2146c58fde70cceee618892714
