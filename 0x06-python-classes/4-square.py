#!/usr/bin/python3
"""define a class square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """Initialize the new square
        arg: size (int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)
