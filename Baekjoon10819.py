import sys

sys.stdin = open("Baekjoon10819.txt")


def choic(paArr):
    if len(paArr) == N:
        global an
        a = 0
        for i in range(N - 1):
            a += abs(paArr[i] - paArr[i + 1])
        an = max(a, an)
    for i in range(N):
        if not vi[i]:
            vi[i] = 1
            choic(paArr + [aa[i]])
            vi[i] = 0


N = int(input())
aa = list(map(int, input().split()))
vi = [0] * N
an = 0
choic([])
print(an)
