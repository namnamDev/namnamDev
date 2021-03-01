import sys
from pprint import pprint
from pprint import pprint

sys.stdin = open("ExpertAcademy4615.txt")

dirx = [1, -1, 0, 0, 1, 1, -1, -1]
diry = [0, 0, 1, -1, 1, -1, -1, 1]


def findreverse(board):  # 변경가능한 방향 서칭
    wx = x + dirx[g]
    wy = y + diry[g]
    while 0 <= wx < N and 0 <= wy < N:
        if board[wx][wy] == color:
            return True
        else:
            wx += dirx[g]
            wy += diry[g]
    return False


def doreverse(dd):  # 대입된 방향으로의 변환 시도
    wx = x + dirx[dd]
    wy = y + diry[dd]
    changelist = []
    while 0 <= wx < N and 0 <= wy < N:
        if board[wx][wy] != color and board[wx][wy] != 0:
            changelist += [(wx, wy)]
            wx += dirx[dd]
            wy += diry[dd]
        else:
            break

    return changelist


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1

    for i in range(M):
        y, x, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        temp = [0] * 8  # 변경가능한 방향을 담을 임시리스트
        for g in range(8):
            if findreverse(board):
                temp[g] = 1

        for gg in range(8):
            change = []
            if temp[gg]:
                change += doreverse(gg)
                for rev in change:
                    board[rev[0]][rev[1]] = color
    one = 0
    two = 0
    for i in board:
        for g in i:
            if g == 1:
                one += 1
            elif g == 2:
                two += 1
    print("#{} {} {}".format(tc, one, two))
