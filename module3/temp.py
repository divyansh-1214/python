from collections import *
# print("heyyy")
# data = (1,2,3,4,5)
# a,*b,c = data
# print(b)
# print(c)


# data = {
#     "name":"Divaynsh",
#     "class" : "3rd year"
# }

# print(data.get("name"))

# enumerate(iterable, start=0)

# data = ["hey","my","name","is","Divyansh"]
# for index, data in enumerate(data):
#     print(index,data)
# it can be only used to get the data and the index but do not modefy it

# def my_gen():
#     print("Start")
#     yield 1
#     print("Middle")
#     yield 2
#     print("End")
#     yield 3


# g = my_gen()
# print(next(g))  # 1
# print(next(g))  # 2

# gen = (x for x in range(1000000))
lst = [x for x in range(5)]   # list comprehension → list
gen = (x for x in range(5))   # generator expression → generator
# gen = ([1,2,3,4,5])
g = gen
# print(lst)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# squares = []
# for i in range(1, 6):
#     squares.append(i*i)
# [expression for item in iterable if condition]

s = [x*x for x in range(1,6)]
even = [x for x in range(1,21) if x%2== 0]

matrix = [[j for j in range(i)] for i in range(3)]
# the inner one is the outer loop and the outer is the inner loop
# matrix = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(j)
#     matrix.append(row)

# nums = [1,2,3,4,5,6,7,8]
# res = [x for x in nums if x%2==0 and x>4]
# print(res)


lst = [1,2,2,3,3,3,4]
c = Counter(lst)
# print(c)
print(c.most_common(2))
d = defaultdict(int)
for i in [1,1,1,2,3,4]:
    d[i] += 1  
print(d)

print(defaultdict(int))   # default = 0
print(defaultdict(list))  # default = []
print(defaultdict(set))   # default = set()

