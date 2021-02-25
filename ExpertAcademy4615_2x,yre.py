import sys
from pprint import pprint
from pprint import pprint

sys.stdin = open("ExpertAcademy4615.txt")

dirx = [1, -1, 0, 0, 1, 1, -1, -1]
diry = [0, 0, 1, -1, 1, -1, -1, 1]


def findreverse(board):
    wx = x + dirx[g]
    wy = y + diry[g]
    print("-----find-----", dirx[g], diry[g])
    for ff in board:
        print(ff)
    while 0 <= wx < N and 0 <= wy < N:
        if board[wx][wy] == color:
            print(color)
            return True
        else:
            wx += dirx[g]
            wy += diry[g]


def doreverse(board):
    print("------do-----")
    wx = x + dirx[g]
    wy = y + diry[g]
    while 0 <= wx < N and 0 <= wy < N:
        for ff in board:
            print(ff)
        if board[wx][wy] != color and board[wx][wy] != 0:
            print(wx, wy)
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
    pprint(board)
    action = [0] * M
    for i in range(M):
        action[i] = list(map(int, input().split()))

    for i in action:
        x, y, color = map(int, i)
        x -= 1
        y -= 1
        board[x][y] = color
        print(x, y)
        temp = [False] * 8
        for g in range(8):
            if findreverse(board):  # 돌이 바뀔수 있는 방향을 우선 탐색하는 함수
                print("----", g, "----")
                temp[g] = True  # 탐색후 해당 dir번호를 temp에 넣고
        print(temp)
        for g in range(8):
            if temp[g]: # 바
                doreverse(board)
    one = 0
    two = 0
    for ii in board:
        for gg in ii:
            if gg == 1:
                one += 1
            elif gg == 2:
                two += 1
    pprint(board)
    print("#{} {} {}".format(tc, one, two))
    # pprint(action)
