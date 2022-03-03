import sys
from pathlib import Path

sys.stdin = open("Baekjoon2239.txt")

from collections import deque


def lec(py, px, pi):
    global bbb
    if not bbb:
        return
    checks = 0
    for yy in range(9):
        for xx in range(9):
            if board[yy][xx]:
                checks += 1
    if checks == 81:  ## 풀 조건을 달성하면?
        for i in board:
            print(i)
        bbb = False  # 글로벌 bbb에 담아줘서 lec가 더이상 동작하지않게.
        return
    for i in board:
        print(i)
    for y in range(9):
        for x in range(9):
            if not board[y][x]:
                tres = [ga(y), se(x), sa(y, x)]  # 가로 , 세로, 사각에 이미 사용된 숫자들리턴해주는 배열들
                tvi = [0] * 9  # 임시 visted 생성
                for i in tres:
                    for ii in range(9):
                        if i[ii] >= 2:  # 만약 2번이상 사용된 숫자가 있다면?
                            print("duplicated", py, px, pi)
                            return
                        if not tvi[ii]:  # 만약 임시 visited가 비어있고 ,
                            if i[ii] == 1:  # 가,세,사 방문횟수가 1이라면
                                tvi[ii] = 1  # tvi 에 방문처리
                if 0 not in tvi:  # 만약 방문가능한 자리가 없다면
                    print("no 0", py, px, pi)  # 그전껄 제거하고 리턴
                    return
                    # print()
                print(tvi, "tvi")
                for inum in range(9):
                    if not tvi[inum]:  # 가,세,사에서 방문 가능한것들 모으고
                        boardCanN[y][x][inum] += 1  # 방문처리시켜놓고
                        board[y][x] = inum + 1
                        print(y, x, inum)
                        lec(y, x, inum)
                        boardCanN[y][x][inum] -= 1
                        board[y][x] = 0
                        # boardCanN[y][x][inum] -= 1
                        # board[y][x] = 0


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
