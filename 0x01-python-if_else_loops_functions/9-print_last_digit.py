#!/usr/bin/python3
def print_last_digit(number):
    number_str = repr(number)
    last_digit_str = number_str[-1]
    last_digit = int(last_digit_str)
    return last_digit
