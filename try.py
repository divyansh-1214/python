from functools import reduce


def sub(a):
    return a - 1


def sum(a, b):
    return a + b


def max(a, b):
    if a > b:
        return a
    else:
        return b


# um = list(map(lambda x: x + 1, [1, 2, 3, 4, 5]))
# new = list()
# print(new)
# um = list(map(sub, [1, 2, 3, 4, 5]))
# print(um)


# reduce frunction
# reduce() reduces a sequence to a single value
# Requires functools module
# Works on iterables
# Function must take two arguments
# Commonly used with lambda functions
# Used for sum, product, max, min
# Supports initial value

# print(reduce(sum, [1, 2, 3, 4, 5]))
# print(reduce(max, [1, 2, 3, 4, 5]))
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# def sayHey():
#     """this function can be used to say hey"""
#     print("Hey there!")
# print(sayHey.__doc__)


def mull(*n):
    """this function multiplies all the numbers"""
    p = 1
    for i in n:
        p = p * i
    return p


def show(**data):
    for k, v in data.items():
        print(f"{k} : {v}")


num = mull(1, 2, 3, 4)
print(num)
show(name="Divyansh", age=20, city="Lucknow")
