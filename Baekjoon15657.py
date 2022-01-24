import sys

sys.stdin = open("Baekjoon15657.txt")


def choic(paArr, paIdx):
    if len(paArr) == M:
        print(*paArr)
        return
    for i in range(paIdx, N):
        choic(paArr + [aa[i]], i)


N, M = map(int, input().split())
aa = list(map(int, input().split()))
aa.sort()
vi = [0] * N
choic([], 0)
