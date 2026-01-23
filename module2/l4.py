# Write a function that accepts any number of arguments and returns their sum.
from functools import reduce


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


def add(x, y):
    return x + y


s = sum([10, 20, 30, 40, 50])
print(s)
print(reduce(lambda x, y: x + y, [10, 20, 30, 40, 50]))
print(reduce(add, [10, 20, 30, 40, 50]))
# sum = sum_all(1, 2, 3, 4, 5)
