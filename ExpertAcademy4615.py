import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5643.txt")


def d1(N):
    v[N] += 1
    tv[N] += 1
    if r.get(N):
        for f in r.get(N):
            if tv[f] == 0:
                d1(f)


def d2(N):
    v[N] += 1
    tv2[N] += 1
    if r2.get(N):
        for f in r2.get(N):
            if tv2[f] == 0:
                d2(f)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())
    v = [0] * (N + 1)
    r = {}
    r2 = {}
    an = 0
    for i in range(M):
        a, b = map(int, input().split())
        r[a] = r.get(a, []) + [b]
        r2[b] = r2.get(b, []) + [a]
    for i in range(1, N + 1):
        tv = [0] * (N + 1)
        tv2 = [0] * (N + 1)
        d1(i)
        d2(i)
        for g in range(1, N + 1):
            tv[g] += tv2[g]
            if tv[g] == 0:
                break
            if g == N:
                an += 1

    print("#{} {}".format(tc, an))
