#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initialize a new square
        args:
        size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """get/set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area of square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define the == comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != comparison to a square"""
        return self.area() != other.area()

    def __it__(self, other):
        """define the < comparison to square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
