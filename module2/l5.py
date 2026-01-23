# Write a function that accepts any number of arguments and returns their sum.
from functools import reduce


def sum_all(*arg):
    total = 0
    for num in arg:
        total += num
    return total


# def sum_all(*arg):
#     sum = reduce(lambda x, y: x + y, arg)
#     return sum
# def sum_all(*arg):
#     return reduce(lambda x, y: x + y, arg)


print(sum_all(1, 2, 3, 4, 5))
