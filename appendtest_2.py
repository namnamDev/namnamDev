import time

start = time.time()
p = []
append = p.append
for i in range(100000000):
    append(i)
print(time.time() - start)
