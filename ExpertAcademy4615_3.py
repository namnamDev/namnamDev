import sys
from pprint import pprint
from pprint import pprint

sys.stdin = open("ExpertAcademy4615.txt")

dirx = [1, -1, 0, 0, 1, 1, -1, -1]
diry = [0, 0, 1, -1, 1, -1, -1, 1]


def findreverse(board):
    wx = x + dirx[g]
    wy = y + diry[g]
    while 0 <= wx < N and 0 <= wy < N:
        if board[wx][wy] == color:
            return True
        else:
            wx += dirx[g]
            wy += diry[g]


def doreverse(board):
    wx = x + dirx[g]
    wy = y + diry[g]
    while 0 <= wx < N and 0 <= wy < N:
        if board[wx][wy] != color and board[wx][wy] != 0:
            board[wx][wy] = color
            wx += dirx[g]
            wy += diry[g]
        else:
            return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    action = [0] * M
    for i in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        temp = [False] * 8
        for g in range(8):
            if findreverse(board):
                temp[g] = True
        for g in range(8):
            if temp[g]:
                doreverse(board)
    one = 0
    two = 0
    for i in board:
        for g in i:
            if g == 1:
                one += 1
            elif g == 2:
                two += 1
    print("#{} {} {}".format(tc, one, two))
