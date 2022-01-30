import sys

sys.stdin = open("Baekjoon10971.txt")


def runs(paArr, idx, cnt):
    global m
    if cnt >= m:
        return
    if len(paArr) == N:
        if board[idx][a]:
            m = min(m, cnt + board[idx][a])
        return
    for ii in range(N):
        if not vi[ii] and board[idx][ii]:
            vi[ii] = 1
            runs(paArr + [ii], ii, cnt + board[idx][ii])
            vi[ii] = 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
m = 1000000 * N * N + 1
for a in range(N):
    vi = [0] * N
    vi[a] = 1
    runs([a], a, 0)
print(m)
