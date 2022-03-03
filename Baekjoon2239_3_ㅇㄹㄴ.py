import sys
from pathlib import Path

sys.stdin = open("Baekjoon2239.txt")

from collections import deque


def lec(py, px, pi):
    global bbb
    if not bbb:
        return
    # print()
    # for i in board:
    #     print(i)
    # tBoard = board.copy()
    checks = 0
    for yy in range(9):
        for xx in range(9):
            if board[yy][xx]:
                # for zz in range(9):
                #     if boardCanN[yy][xx][zz] >= 2:
                #         return
                checks += 1
    if checks == 81:
        for i in board:
            print(i)
        bbb = False
        return
    for y in range(9):
        for x in range(9):
            if not board[y][x]:
                tres = [ga(y), se(x), sa(y, x)]
                tvi = [0] * 9
                for i in tres:
                    for ii in range(9):
                        if i[ii] >= 2:
                            board[py][px] = 0
                            boardCanN[py][px][pi] -= 1
                            return
                        if not tvi[ii]:
                            if i[ii] == 1:
                                tvi[ii] = 1
                if 0 not in tvi:
                    board[py][px] = 0
                    boardCanN[py][px][pi] -= 1
                    print("no 0", py, px, pi)
                    return
                # for c in range(9):
                #     if not boardCanN[y][x][c]:
                #         tcnt += 1
                print()
                print(tvi)
                for inum in range(9):
                    if not tvi[inum]:
                        boardCanN[y][x][inum] += 1
                        board[y][x] = inum + 1
                        print(y, x, inum)
                        for iii in board:
                            print(iii)
                        lec(y, x, inum)
                        boardCanN[y][x][inum] -= 1
                        board[y][x] = 0
                        print("deleted", y, x, inum)
                

def cou(pavi):
    res = []
    for s in range(9):
        if not pavi[s]:
            res.append(s)
    return res


def ga(y):
    vi = [0] * 9
    for i in range(9):
        if board[y][i]:
            vi[board[y][i] - 1] += 1
    return vi


def se(x):
    vi = [0] * 9
    for i in range(9):
        if board[i][x]:
            vi[board[i][x] - 1] += 1
    return vi


def sa(y, x):
    sy = y // 3 * 3
    sx = x // 3 * 3
    vi = [0] * 9
    for yy in range(sy, sy + 3):
        for xx in range(sx, sx + 3):
            if board[yy][xx]:
                vi[board[yy][xx] - 1] += 1
    return vi


board = [list(map(int, input())) for _ in range(9)]
an = []
boardVi = [[0] * 9 for _ in range(9)]
boardCanN = [[[0] * 9 for _ in range(9)] for _ in range(9)]
bbb = True
lec(0, 0, 0)
# Q = deque([])
# for y in range(9):
#     for x in range(9):
#         if not board[y][x]:
#             Q.append([y, x])
# while Q:
#     tBoard = board.copy()
#     now = Q.popleft()
#     y = now[0]
#     x = now[1]
#     if not board[y][x]:
#         tres = [ga(y), se(x), sa(y, x)]
#         for i in tres:
#             for ii in range(9):
#                 if i[ii]:
#                     boardCanN[y][x][ii] = 1
#         tcnt = 0
#         tN = 0
#         for c in range(9):
#             if not boardCanN[y][x][c]:
#                 tcnt += 1
#                 tN = c
#
#         if tcnt > 1:
#             Q.append([y, x])
#         elif tcnt == 1:
#             boardCanN[y][x][tN] = 1
#             board[y][x] = tN + 1
#     for i in board:
#         print(i)
# print()
# tChange = 0
# for y in range(9):
#     for x in range(9):
#         if board[y][x] != tBoard[y][x]:
#             tChange += 1
# if not tChange:
#     break
# print(Q)
# while Q:
#     tBoard = board.copy()
#     tBoardCanN = boardCanN.copy()
#     now = Q.popleft()
#     y = now[0]
#     x = now[1]
#     for c in range(9):
#         if not boardCanN[y][x][c]:
#             tBoard[y][x] = c + 1
#             tBoardCanN[y][x][c] += 1
# for i in board:
#     print(i)
# for ii in an:
#     print()
#     for i in ii:
#         print(i)
