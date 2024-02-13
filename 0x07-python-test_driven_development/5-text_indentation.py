#!/usr/bin/python3
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
