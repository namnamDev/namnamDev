import sys

sys.stdin = open('Baekjoon16948.txt')
from collections import deque

drx = [-2, -2, 0, 0, 2, 2]
dry = [-1, 1, -2, 2, -1, 1]
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[0] * N for _ in range(N)]
board[c1][r1] = 1
Q = deque([[c1, r1]])

while Q:
    now = Q.popleft()
    for i in range(6):
        wy = now[0] + dry[i]
        wx = now[1] + drx[i]
        if 0 <= wy < N and 0 <= wx < N and not board[wy][wx]:
            board[wy][wx] = board[now[0]][now[1]] + 1
            Q.append([wy, wx])
            if board[c2][r2]:
                Q = []
                break
print(board[c2][r2] - 1)
