import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")

from collections import deque


def lec():
    temp = count_zero()
    if temp:
        print()
        for i in board:
            print(i)

        y = temp[0]
        x = temp[1]
        boardVi[y][x] = 1
        vi = [0] * 9
        tres = [ga(y), se(x), sa(y, x)]
        print(y, x)
        for tarr in tres:
            print(tarr)
            for a in tarr:
                vi[a] += 1
        print(vi)
        if 3 not in vi:
            print("crush!", y, x)
            return
        for ii in range(9):
            if vi[ii] == 3:
                board[y][x] = ii + 1
                lec()
        #         board[y][x] = 0
        # boardVi[y][x] = 0
    else:
        an.append(board.copy())

        return


def count_zero():
    for yy in range(9):
        for xx in range(9):
            if not board[yy][xx]:
                return [yy, xx]
    return []


def cou(pavi):
    res = []
    for s in range(9):
        if not pavi[s]:
            res.append(s)
    return res


def ga(y):
    res = []
    vi = [0] * 9
    for i in range(9):
        if board[y][i]:
            vi[board[y][i] - 1] = 1
    for i in range(9):
        if not vi[i]:
            res.append(i)
    return res


def se(x):
    res = []
    vi = [0] * 9
    for i in range(9):
        if board[i][x]:
            vi[board[i][x] - 1] = 1
    for i in range(9):
        if not vi[i]:
            res.append(i)
    return res


def sa(y, x):
    sy = y // 3 * 3
    sx = x // 3 * 3
    vi = [0] * 9
    for yy in range(sy, sy + 3):
        for xx in range(sx, sx + 3):
            if board[yy][xx]:
                vi[board[yy][xx] - 1] = 1
    res = []
    for i in range(9):
        if not vi[i]:
            res.append(i)
    return res


board = [list(map(int, input())) for _ in range(9)]
an = []
boardVi = [[0] * 9 for _ in range(9)]
# while not an:
lec()
print("fin")
for ii in an:
    print()
    for i in ii:
        print(i)
