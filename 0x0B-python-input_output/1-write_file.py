#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    Args:
        filename: name of the file to write
        text: text to write
    Returns:
        Number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
