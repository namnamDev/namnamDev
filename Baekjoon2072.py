import sys
from collections import deque

sys.stdin = open("Baekjoon2072.txt")
N = int(input())
board = [[0] * 20 for _ in range(20)]
# 흑 1
# 백 2
turn = 1
an = -1
dy = [1, 1, 0, 1]
dx = [0, 1, 1, -1]
for n in range(1, N + 1):
    y, x = map(int, input().split())
    board[y][x] = turn
    for d in range(4):
        cnt = 1
        wy1 = y + dy[d]
        wx1 = x + dx[d]
        wy2 = y - dy[d]
        wx2 = x - dx[d]
        while 0 <= wy1 < 20 and 0 <= wx1 < 20 and board[wy1][wx1] == turn:
            cnt += 1
            wy1 += dy[d]
            wx1 += dx[d]
        while 0 <= wy2 < 20 and 0 <= wx2 < 20 and board[wy2][wx2] == turn:
            cnt += 1
            wy2 -= dy[d]
            wx2 -= dx[d]
        if cnt == 5:
            an = n
            break
    if an > 0:
        break
    turn = 2 if turn == 1 else 1
print(an)
