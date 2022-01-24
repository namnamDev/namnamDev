import sys

sys.stdin = open("Baekjoon16935.txt")


def fiR(paArr):
    tN = len(paArr)
    temp = []
    for ii in range(tN - 1, -1, -1):
        temp.append(paArr[ii])
    return temp


def seC(paArr):
    tN = len(paArr)
    tM = len(paArr[0])
    temp = [[0] * tM for _ in range(tN)]
    for y in range(tN):
        for x in range(tM):
            temp[y][x] = paArr[y][tM - 1 - x]

    return temp


def tiR(paArr):
    tN = len(paArr)
    tM = len(paArr[0])
    temp = [[0] * tN for _ in range(tM)]
    for y in range(tM):
        for x in range(tN):
            temp[y][x] = paArr[tN - 1 - x][y]
    return temp


def foU(paArr):
    tN = len(paArr)
    tM = len(paArr[0])
    temp = [[0] * len(paArr) for _ in range(len(paArr[0]))]
    for y in range(tM):
        for x in range(tN):
            temp[y][x] = paArr[x][tM - 1 - y]
    return temp


def fiV(paArr):
    tN = len(paArr)
    tM = len(paArr[0])
    temp = [[0] * tM for _ in range(tN)]
    for y in range(tN // 2):
        for x in range(tM // 2):
            temp[y][x] = paArr[y + tN // 2][x]
            temp[y + tN // 2][x] = paArr[y + tN // 2][x + tM // 2]
            temp[y + tN // 2][x + tM // 2] = paArr[y][x + tM // 2]
            temp[y][x + tM // 2] = paArr[y][x]
    return temp


def siX(paArr):
    tN = len(paArr)
    tM = len(paArr[0])
    temp = [[0] * tM for _ in range(tN)]
    for y in range(tN // 2):
        for x in range(tM // 2):
            temp[y][x] = paArr[y][x + tM // 2]
            temp[y][x + tM // 2] = paArr[y + tN // 2][x + tM // 2]
            temp[y + tN // 2][x + tM // 2] = paArr[y + tN // 2][x]
            temp[y + tN // 2][x] = paArr[y][x]
    return temp


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))
for n in range(R):
    if arr[n] == 1:
        board = fiR(board)
    elif arr[n] == 2:
        board = seC(board)
    elif arr[n] == 3:
        board = tiR(board)
    elif arr[n] == 4:
        board = foU(board)
    elif arr[n] == 5:
        board = fiV(board)
    else:
        board = siX(board)
for i in board:
    print(*i)
