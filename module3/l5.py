# Use Counter from the collections module to count occurrences of each element in a list.
from collections import *
lst = [1,2,2,3,3,3,4]
c = Counter(lst)
print(c)