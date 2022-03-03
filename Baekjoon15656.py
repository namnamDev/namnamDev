import sys

sys.stdin = open("Baekjoon15656.txt")


def cho(paArr):
    if len(paArr) == M:
        print(*paArr)
        return
    for i in range(N):
        cho(paArr + [arr[i]])


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cho([])
