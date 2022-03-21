import sys

sys.stdin = open("Baekjoon14442.txt")
from collections import deque

N, M, K = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
vi = [[0] * M for _ in range(N)]
vi[0][0] = 1
Q = deque([[0, 0, 0]])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while Q:
    y, x, b = Q.popleft()
    for d in range(4):
        wy = y + dy[d]
        wx = x + dx[d]
        if 0 <= wy < N and 0 <= wx < M and not vi[wy][wx]:
            t = b
            if board[wy][wx]:
                t += 1
            vi[wy][wx] = 1 + vi[y][x]
            if t <= K:
                Q.append([wy, wx, t])

if not vi[-1][-1]:
    vi[-1][-1] = -1
print(vi[-1][-1])
# for i in board:
#     print(i)
# print()
# for i in vi:
#     print(i)
# if not vi[-1][-1]:
#     vi[-1][-1] = -1
#
# print(vi[-1][-1])
