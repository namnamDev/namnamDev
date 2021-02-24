import sys

sys.stdin = open("ExpertAcademy1859.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxIdx = 0
    dpli = [0] * N
    i = 0
    while i < N:
        maxN = arr[i]
        maxIdx = i
        for g in range(i + 1, N):
            if maxN < arr[g]:
                maxN = arr[g]
                maxIdx = i
        dpli[i] = maxN - arr[i]

        if maxIdx != i:
            i = maxIdx
        else:
            i += 1

    print("#{} {}".format(tc, sum(dpli)))
