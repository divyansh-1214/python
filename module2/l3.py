# Use filter to extract even numbers from a list.
print("love you")


def is_even(n):
    return n % 2 == 0


numbers = list(range(1, 21))
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
print(list(filter(lambda x: x % 2 == 0, numbers)))

# flter(function, iterable)
# Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.
