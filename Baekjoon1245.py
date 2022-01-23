import sys

sys.stdin = open("Baekjoon1245.txt")
from collections import deque

dy = [-1, 1, 0, 0, -1, 1, 1, -1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
vi = [[0] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if not vi[y][x] and board[y][x]:
            temp = board[y][x]
            vi[y][x] = 1
            Q = deque([[y, x]])
            cnt = [board[y][x], y, x]
            while Q:
                now = Q.popleft()
                for d in range(8):
                    wy = now[0] + dy[d]
                    wx = now[1] + dx[d]
                    if 0 <= wy < N and 0 <= wx < M and not vi[wy][wx]:
                        vi[wy][wx] = 1
                        Q.append([wy, wx])
