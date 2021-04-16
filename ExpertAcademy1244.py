import sys
import time

sys.stdin = open("ExpertAcademy1244.txt")

start = time.time()


# 첫제출(시간초과)
def powerset(arr, cnt):
    if cnt == change:
        global res
        global maxs
        an = ''
        for f in arr:
            an += f
        maxs += 1
        print(an, maxs)
        res.append(int(an))
        return
    tarr = arr.copy()
    for g in range(len(arr)):
        for f in range(len(arr)):
            if f != g:
                tarr[f], tarr[g] = tarr[g], tarr[f]
                powerset(tarr, cnt + 1)


for tc in range(int(input())):
    maxs = 0
    num, change = input().split()
    num = list(num)
    change = int(change)
    res = []
    powerset(num, 0)
    print(len(res), res)
    print("#{} {}".format(tc + 1, max(res)))
print('time', time.time() - start)
