#!/usr/bin/python3
"""class Squaare that iherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of a square"""
    def __init__(self, size):
        """instatiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of the square"""
        return self.__size ** 2
