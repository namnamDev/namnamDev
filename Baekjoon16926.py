import sys
from collections import deque

sys.stdin = open("Baekjoon16926.txt")


def rec(ys, ye, xs, xe):
    if ys == ye or xs == xe:
        return
    arr = []
    for y in range(ys, ye):
        arr.append([y, xs, board[y][xs]])
    for x in range(xs + 1, xe):
        arr.append([ye - 1, x, board[ye - 1][x]])
    for y in range(ye - 2, ys - 1, -1):
        arr.append([y, xe - 1, board[y][xe - 1]])
    for x in range(xe - 2, xs, -1):
        arr.append([ys, x, board[ys][x]])
    for i in range(len(arr)):
        now = arr[i]
        changed = arr[i - R % len(arr)]
        board[now[0]][now[1]] = changed[2]
    rec(ys + 1, ye - 1, xs + 1, xe - 1)


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rec(0, N, 0, M)
for i in board:
    print(*i)
