#!/usr/bin/python3
"""function returns True if object is instance of class"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class else false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
