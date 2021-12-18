import sys

sys.stdin = open('Baekjoon15666.txt')


def back(arr, idx):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(idx, len(a)):
        back(arr + [a[i]], i)


N, M = map(int, input().split())
a = sorted(list(set(list(map(int, input().split())))))
back([], 0)
