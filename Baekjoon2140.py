import sys

sys.stdin = open('Baekjoon2140.txt')
from collections import deque

N = int(input())
board = [list(input()) for _ in range(N)]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, 1, -1, -1, 1]
fines = [[0] * N for _ in range(N)]
Q = deque([])
for y in range(N):
    for x in range(N):
        if board[y][x] == "#":
            board[y][x] = -2
        Q.append([y, x])
while Q:
    y, x = map(int, Q.popleft())
    if not fines[y][x] and int(board[y][x]) >= 0:
        arrMines = int(board[y][x])
        arr = []
        mines = 0
        for d in range(8):
            wy = dy[d] + y
            wx = dx[d] + x
            if 0 <= wy < N and 0 <= wx < N:
                if board[wy][wx] == -2:
                    arr.append([wy, wx])
                elif board[wy][wx] == -3:
                    mines += 1
        nonBlockCnt = len(arr)
        if nonBlockCnt == arrMines - mines:
            fines[y][x] = 1
            for c in range(nonBlockCnt):
                board[arr[c][0]][arr[c][1]] = -3
                fines[arr[c][0]][arr[c][1]] = 1
        if mines == arrMines:
            fines[y][x] = 1
            for c in range(nonBlockCnt):
                board[arr[c][0]][arr[c][1]] = -1
                fines[arr[c][0]][arr[c][1]] = 1
        if not fines[y][x]:
            Q.append([y, x])
an = 0
for y in range(N):
    for x in range(N):
        if int(board[y][x]) <= -2:
            an += 1
print(an)
