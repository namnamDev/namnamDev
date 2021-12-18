import sys

sys.stdin = open('Baekjoon15651.txt')


def back(arr, cnt):
    if cnt == M:
        print(*arr)
        return
    for i in range(N):
        back(arr + [i + 1], cnt + 1)


N, M = map(int, input().split())
back([], 0)
