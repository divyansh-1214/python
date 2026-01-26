print("hey")
# Create a list of first 10 natural numbers using list comprehension.
# [expression for item in iterable if condition]
list = [x for x in range(1,11)]
print(list)
# Create a list of squares of numbers from 1 to 10.
sq_list = [x*x for x in range(1,11)]
print(sq_list)
# Create a list of even numbers between 1 and 20.
even_list = [x for x in range(1,21) if x%2 == 0]
print(even_list)
# Create a new list containing only odd numbers.
# nums = [1, 2, 3, 4, 5]
odd_lsit = [x for x in [1, 2, 3, 4, 5] if x%2 != 0]
print(odd_lsit)
# Convert this list into a list of strings:
# lst = [1, 2, 3, 4]
string_list = [str(x) for x in [1,2,3,4] ]
print(string_list)
# nums = [2, 5, 8, 11, 14, 17]
# Create a list of numbers greater than 10.
larger_than_10 = [x for x in [2, 5, 8, 11, 14, 17] if x > 10]
print(larger_than_10)
# s = "programming"
# Create a list of vowels present in the string.
vowel_list = [x for x in "programming" if x in "aeiou"]
print(vowel_list)
# Create a list of lengths of each word:
# words = ["Python", "is", "very", "easy"]
lenght_list = [len(x) for x in ["Python", "is", "very", "easy"]]
print(lenght_list)

# nums = [1, 2, 3, 4, 5]
# Create a list where:
# if number is even → "Even"
# else → "Odd"
oe_list = ["Even" if x %2 ==0 else "odd"  for x in range(1,6,1) ]
print(oe_list)
# Flatten this list using list comprehension:
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
list = [y for x in [[1,2,3], [4,5,6], [7,8,9]] for y in x ]
print(list)
# Remove vowels from a string using list comprehension:
# s = "engineering"
v_list = [x for x in "engineering" if x in "aeiou"]
print(v_list)
# lst = [10, 20, 30, 40, 50]
# Create a list where each element is increased by 10 only if it is greater than 25.
inc_list = [x+25 if x > 25 else x for x in [10, 20, 30, 40, 50] ]
print(inc_list)
# names = ["Divyansh", "Rahul", "Amit", "Rohit"]
# Create a list of names whose length is greater than 4.
list_greater_4 = [x for x in ["Divyansh", "Rahul", "Amit", "Rohit"] if len(x) > 4]
print(list_greater_4)
# Create a 3×3 identity matrix using list comprehension.
matrix = [[1 if x == y else 0  for y in range(3)] for x in range(3)]
print(matrix)
# Extract digits from this string:
# s = "a1b2c3"
d_list = [int(x) for x in "a1b2c3" if x in "0123456789"]
print(d_list)
