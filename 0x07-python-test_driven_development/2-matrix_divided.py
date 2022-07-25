#!/usr/bin/python3
"""Define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): List of list of integers or floats
        div (int/float): the divider
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not int or float
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix
        """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix(list of list) of"
                        "integer/float")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
