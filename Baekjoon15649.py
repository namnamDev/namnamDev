import sys

sys.stdin = open('Baekjoon15649.txt')


def choi(arr, depth, idx):
    if depth == M:
        print(*arr)
        return
    for i in range(idx, N):
        if not vi[i]:
            vi[i] = 1
            choi(arr + [i + 1], depth + 1, i + 1)
            vi[i] = 0


N, M = map(int, input().split())
vi = [0] * N
choi([], 0, 0)
