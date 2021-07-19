import sys

sys.stdin = open('Baekjoon15663.txt')


def choices(pArr, depth):
    if depth == M:
        print(*pArr)
        return
    for i in range(N):
        if not vi[i]:
            vi[i] = 1
            if not di.get(str(pArr + [arr[i]])):
                di[str(pArr + [arr[i]])] = pArr + [arr[i]]
                choices(pArr + [arr[i]], depth + 1)
            vi[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = []
vi = [0] * N
di = {}
choices([], 0)
