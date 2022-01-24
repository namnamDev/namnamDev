import sys

sys.stdin = open("Baekjoon15654.txt")


def choic(paArr):
    if len(paArr) == M:
        print(*paArr)
    for i in range(N):
        if not vi[i]:
            vi[i] = 1
            choic(paArr + [aa[i]])
            vi[i] = 0


N, M = map(int, input().split())
aa = list(map(int, input().split()))
aa.sort()
vi = [0] * N
choic([])
