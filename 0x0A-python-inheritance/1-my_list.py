#!/usr/bin/python3
"""defining class Mylist"""


class MyList(list):
    """defining function print_sorted"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
