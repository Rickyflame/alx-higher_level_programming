#!/usr/bin/pyhton3
"""define a class"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """Initialize a new square
        args: size (int): size of new square
        """
        self.__size = size

    @property
    def size(self):
        """get the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
