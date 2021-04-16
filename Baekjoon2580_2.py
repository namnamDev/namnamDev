import sys
import time

sys.stdin = open('Baekjoon2580.txt')

board = [list(map(int, input().split())) for _ in range(9)]


def sdoku(y, x):
    box = []
    boxy = (y // 3) * 3
    boxx = (x // 3) * 3
    boxsum = 0
    for f in range(3):
        for g in range(3):
            box.append([board[boxy + f][boxx + g], [boxy + f, boxx + g]])
            boxsum += board[boxy + f][boxx + g]
    row = []
    row_0 = []
    col = []
    col_0 = []
    box_0 = []
    for i in range(9):
        row.append(board[y][i])
        col.append(board[i][x])
        if not board[y][i]:
            row_0.append([y, i])
        if not board[i][x]:
            col_0.append([i, x])
        if not box[i][0]:
            box_0.append(box[i][1])

    if len(row_0) == 1:
        board[row_0[0][0]][row_0[0][1]] = 45 - sum(row)
        return
    if len(col_0) == 1:
        board[col_0[0][0]][col_0[0][1]] = 45 - sum(col)
        return
    if len(box_0) == 1:
        board[box_0[0][0]][box_0[0][1]] = 45 - boxsum
        return

    for i in range(9):
        if not board[y][i]:
            sdoku(y, i)
        if not board[i][x]:
            sdoku(i, x)
        if not board[box[i][0], box[i][1]]:
            sdoku(box[i][0], box[i][1])

        # 36 37 38 // 0 1 2
        # 46 47 48 // 3 4 5
        # 56 57 58 // 6 7 8
    # col = []

    # for g in range(9):
    #     col.append(board[g][i[1]])


visited = [[0] * 9 for _ in range(9)]
for i in range(9):
    for g in range(9):
        if not board[i][g]:
            sdoku(i, g)

for i in board:
    print(*i)
