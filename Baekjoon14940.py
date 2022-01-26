import sys

sys.stdin = open("Baekjoon14940.txt")

from collections import deque


def countFlag():
    for y in range(n):
        for x in range(m):
            if board[y][x] == 2:
                return [y, x]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
vi = [[-2] * m for _ in range(n)]
start = countFlag()
vi[start[0]][start[1]] = 0
Q = deque([start])
Q2 = deque([])
while Q:
    now = Q.popleft()
    for d in range(4):
        wy = dy[d] + now[0]
        wx = dx[d] + now[1]
        if 0 <= wy < n and 0 <= wx < m and vi[wy][wx] == -2:
            if board[wy][wx]:
                Q.append([wy, wx])
                vi[wy][wx] = vi[now[0]][now[1]] + 1
            else:
                vi[wy][wx] = 0
                Q2.append([wy, wx])
while Q2:
    now = Q2.popleft()
    for d in range(4):
        wy = dy[d] + now[0]
        wx = dx[d] + now[1]
        if 0 <= wy < n and 0 <= wx < m and vi[wy][wx] == -2:
            if not board[wy][wx]:
                vi[wy][wx] = 0
            else:
                vi[wy][wx] += 1
            Q2.append([wy, wx])
for ii in vi:
    print(*ii)
