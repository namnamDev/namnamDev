import sys

sys.stdin = open('Baekjoon1245.txt')

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
vi = [[0] * M for _ in range(N)]
for i in board:
    print(i)
dy = [-1, 1, -1, 1, 0, 0, -1, 1]
dx = [-1, 1, 1, -1, -1, 1, 0, 0]

y = 0
x = 0
vi[y][x] = 1
Q = deque([[y, x]])
i = 1
while Q:
    now = Q.popleft()
    for d in range(8):
        wy = now[0] + dy[d]
        wx = now[1] + dx[d]
        if 0 <= wy < N and 0 <= wx < M and not vi[wy][wx] and board[wy][wx]:
            vi[wy][wx] = 1
            Q.append([wy, wx])
            # if board[wy][wx] == i:
            #     Q.append([wy, wx])
            # elif board[wy][wx] > i:
            #     i = board[wy][wx]
            #     Q = deque([[wy, wx]])
print()
for i in vi:
    print(i)
