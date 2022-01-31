import sys

sys.stdin = open("Baekjoon2636.txt")
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
an = 0
annn = N * M
while annn:
    vi = [[0] * M for _ in range(N)]
    y = 0
    x = 0
    ann = 0
    for yy in board:
        for xx in yy:
            if xx:
                ann += 1
    if not ann:
        break
    else:
        annn = ann
    an += 1
    Q = deque([[y, x]])
    while Q:
        now = Q.popleft()
        for d in range(4):
            wy = now[0] + dy[d]
            wx = now[1] + dx[d]
            if 0 <= wy < N and 0 <= wx < M and not vi[wy][wx]:
                vi[wy][wx] = 1
                if board[wy][wx]:
                    board[wy][wx] = 0
                else:
                    Q.append([wy, wx])
print(an)
print(annn)
