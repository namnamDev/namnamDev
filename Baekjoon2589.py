import sys

sys.stdin = open("Baekjoon2589.txt")
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
an = 0
for y in range(Y):
    for x in range(X):
        if board[y][x] == "L":
            Q = deque([[y, x]])
            vi = [[0] * X for _ in range(Y)]
            vi[y][x] = 1
            last = [y, x]
            while Q:
                now = Q.popleft()
                for d in range(4):
                    wy = now[0] + dy[d]
                    wx = now[1] + dx[d]
                    if 0 <= wy < Y and 0 <= wx < X and board[wy][wx] == "L" and not vi[wy][wx]:
                        vi[wy][wx] = vi[now[0]][now[1]] + 1
                        last = [wy, wx]
                        Q.append([wy, wx])
            an = max(an, vi[last[0]][last[1]])
print(an - 1)
