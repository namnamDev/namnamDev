import sys

sys.stdin = open("ExpertAcademy11545.txt")
from collections import deque

diry = [0, 0, -1, 1, - 1, 1, -1, 1]
dirx = [-1, 1, 0, 0, 1, -1, -1, 1]
T = int(input())
for tc in range(T):
    board = [list(input()) for _ in range(4)]
    Xcnt = 0
    Ocnt = 0
    Tis = [5, 5]
    if tc != T - 1:
        skip = input()
    for i in range(4):
        for g in range(4):
            if board[i][g] == 'X':
                Xcnt += 1
            elif board[i][g] == 'O':
                Ocnt += 1
            elif board[i][g] == 'T':
                Tis = [i, g]
    print(Xcnt, Ocnt, Tis[0], Tis[1])
    whosturn = ''
    if Tis[0] < 5 and Tis[1] < 5:
        if Xcnt <= Ocnt:
            whosturn = 'O'
            # board[Tis[0]][Tis[1]] = 'O'
        elif Xcnt > Ocnt:
            whosturn = 'X'
            # board[Tis[0]][Tis[1]] = 'X'
    for fff in board:
        print(fff)
    for i in range(4):
        for g in range(4):
            print('xxxx', i, g, tc)
            print(board[i][g])
            if board[i][g] == whosturn:
                start = [0, 0]  # whosturn ==
                vi = [[0] * 4 for _ in range(4)]
                Q = deque([start])
                vi[start[0]][start[1]] = 1
                while Q:
                    now = Q.popleft()
                    for dir in range(8):
                        wy = now[0] + diry[dir]
                        wx = now[1] + dirx[dir]
                        if 0 <= wy < 4 and 0 <= wx < 4 and board[wy][wx] == whosturn and not vi[wy][wx]:
                            Q.append([wy, wx])
                            vi[wy][wx] = 1 + vi[now[0]][now[1]]
                for ff in vi:
                    print(ff)
