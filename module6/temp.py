from datetime import date,datetime,time
import time 
print("hey my name is Divyansh")

d = date.today()
print(d)              # current date
print(d.year)
print(d.month)
print(d.day)
# t = time()
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
now = datetime.now()
print(now)

start = time.perf_counter()
for i in range(1000000):
    pass
end = time.perf_counter()
print(end - start)