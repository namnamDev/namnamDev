import sys
from collections import deque

sys.stdin = open("Baekjoon16926.txt")


def rec(ys, ye, xs, xe):
    if ys == ye or xs == xe:
        # print("no")
        return
    arr = []
    # tArr2 = []
    for y in range(ys, ye):
        arr.append([y, xs, board[y][xs]])
        # tArr2.append(board[y][xs])
    for x in range(xs + 1, xe):
        arr.append([ye - 1, x, board[ye - 1][x]])
        # tArr2.append(board[ye - 1][x])
    for y in range(ye - 2, ys - 1, -1):
        arr.append([y, xe - 1, board[y][xe - 1]])
        # tArr2.append(board[y][xe - 1])
    for x in range(xe - 2, xs, -1):
        arr.append([ys, x, board[ys][x]])
        # tArr2.append(board[ys][x])
    print(ys, ye, xs, xe, arr, len(arr), R, R % len(arr))
    tArr = []
    cnt = 0
    for i in range(len(arr)):
        now = arr[i]
        changed = arr[i - R % len(arr)]
        board[now[0]][now[1]] = changed[2]
        cnt += 1
        tArr.append(changed[2])
    # print(tArr2)
    print(tArr)
    rec(ys + 1, ye - 1, xs + 1, xe - 1)


N, M, R = map(int, input().split())
print(N, M, R)
board = [list(map(int, input().split())) for _ in range(N)]
for i in board:
    print(i)
print()
rec(0, N, 0, M)
for i in board:
    print(i)
# rec(1, N - 1, 1, M - 1)
# rec(2, N - 2, 2, M - 2)
# ys = 0
# ye = N
# xs = 0
# xe = M
# arr = []
# for y in range(ys, ye):
#     arr.append(board[y][xs])
# for x in range(xs + 1, xe):
#     arr.append(board[ye - 1][x])
# for y in range(ye - 2, ys - 1, -1):
#     arr.append(board[y][xe - 1])
# for x in range(xe - 2, xs, -1):
#     arr.append(board[ys][x])
# print(arr)
