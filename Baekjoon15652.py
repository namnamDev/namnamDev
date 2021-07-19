import sys

sys.stdin = open('Baekjoon15652.txt')


def cho(arr, depth, idx):
    if depth == M:
        print(*arr)
        return
    for i in range(idx, N):
        cho(arr + [i + 1], depth + 1, i)


N, M = map(int, input().split())
cho([], 0, 0)
