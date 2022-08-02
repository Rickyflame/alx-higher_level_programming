#!/usr/bin/python3
"""Defines function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file.

    Args:
        filename: name of the file to append to.
        text: string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
