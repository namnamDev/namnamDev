size = 10001
vi = [0] * size
vi[0] = vi[1] = 1
for i in range(2, size):
    if not vi[i]:
        t = i * 2
        while t < size:
            vi[t] = 1
            t += i
T = int(input())
for tc in range(T):
    t = int(input())
    minGap = t
    anFir = anSec = 0
    for fir in range(2, t // 2 + 1):
        sec = t - fir
        if not vi[fir] and not vi[sec]:
            if minGap > sec - fir:
                anFir, anSec = fir, sec
                minGap = sec - fir
    print(anFir, anSec)