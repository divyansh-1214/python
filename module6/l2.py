import time

start = time.perf_counter()

# some code
for i in range(1000000):
    pass

end = time.perf_counter()

print(end - start)
