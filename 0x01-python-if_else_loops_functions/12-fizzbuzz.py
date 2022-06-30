#!/usr/bin/python3
str1 = "Fizz"
str2 = "Buzz"


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("%s%s" % (str1, str2), end=' ')
        elif (i % 3 == 0):
            print("%s" % (str1), end=' ')
        elif (i % 5 == 0):
            print("%s" % (str2), end=' ')
        else:
            print("%d" % (i), end=' ')
