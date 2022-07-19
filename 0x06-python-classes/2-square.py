#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents the square"""
    def __init__(self, size=0):
        """Initialize the square"""
        if not isinstance(size, int):
            raise TypeError("size must ne an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
