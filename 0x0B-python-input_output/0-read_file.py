#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Prints UTF8 text file contents to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
