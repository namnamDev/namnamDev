import sys
import time

sys.stdin = open("ExpertAcademy1244.txt")


def myfunction(arr, cnt):
    if cnt == change:
        global res
        global testarr
        temp = int(''.join(arr))
        res = max(res, temp)
        testarr.append(temp)
        return
    tarr = arr.copy()
    for g in range(len(arr)):
        for f in range(len(arr)):
            if g != f:
                tarr[f], tarr[g] = tarr[g], tarr[f]
                temp = ''.join(tarr)
                if memo.get((temp, cnt), True):
                    memo[(temp, cnt)] = 0
                    myfunction(tarr, cnt + 1)
                tarr[f], tarr[g] = tarr[g], tarr[f]


for tc in range(int(input())):
    num, change = input().split()
    num = list(num)
    change = int(change)
    res = 0
    memo = {}
    testarr = []
    myfunction(num, 0)
    print(testarr)
    testset = set(testarr)
    print(len(testset), len(memo), testset)
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
