import sys
import time

sys.stdin = open("ExpertAcademy1244.txt")


def myfunction(arr, cnt):
    if cnt == change:
        global res
        temp = int(''.join(arr))
        res = max(res, temp)
        return
    for g in range(len(arr) - 1):
        for f in range(g + 1, len(arr)):
            arr[f], arr[g] = arr[g], arr[f]
            temp = ''.join(arr)
            if memo.get((temp, cnt), True):
                memo[(temp, cnt)] = 0
                myfunction(arr, cnt + 1)
            arr[f], arr[g] = arr[g], arr[f]


for tc in range(int(input())):
    num, change = input().split()
    num = list(num)
    change = int(change)
    res = 0
    memo = {}
    myfunction(num, 0)
    print("#{} {}".format(tc + 1, res))
# 1 321
# 2 7732
# 3 857147
# 4 87664
# 5 88832
# 6 777770
# 7 966354
# 8 954311
# 9 332211
# 10 987645
