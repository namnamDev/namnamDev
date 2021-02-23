import sys

sys.stdin = open("ExpertAcademy3307.txt")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))
    dpli = [1] * (N)
    dpli[1] = 1
    for i in range(1, N):
        for g in range(i - 1, -1, -1):
            if li[g] <= li[i]:
                print(g, i, li[g], li[i])
                tempMax = 1
                for f in range(1, i):
                    temp = 0
                    if li[f] <= li[g]:
                        temp = dpli[f]
                    if tempMax < temp:
                        tempMax = temp
                        print(tempMax)
                dpli[i] = tempMax + 1
                break
    print(dpli)
