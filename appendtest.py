import time

for g in range(10):
    start = time.time()  # 시작 시간 저장
    p = []
    for i in range(1000):
        p.append(i)
    time1 = time.time() - start
    start = time.time()
    p = []
    append = p.append
    for i in range(1000):
        append(i)
    time2 = time.time() - start
    print("#{} {}".format(g, time1 - time2))
