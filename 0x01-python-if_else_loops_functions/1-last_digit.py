#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# get the string representation
number_str = repr(number)
#access the last string of the digit string
last_digit_str = number_str[-1]
#convert the last digit string to an integer
last_digit = int(last_digit_str)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
