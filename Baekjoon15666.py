import sys

sys.stdin = open('Baekjoon15666.txt')


def back(arr, idx):
    if len(arr) == M:
        if arr not in an:
            an.append(arr)
        return
    for i in range(idx, N):
        back(arr + [a[i]], i)


N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
an = []
back([], 0)
for g in an:
    print(*g)
