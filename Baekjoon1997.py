import sys

sys.stdin = open("Baekjoon1997.txt")
n, w, b = map(int, input().split())
arrN = []
arrL = []
board = [["ㅁ"] * w for _ in range(b)]
for _ in range(n):
    temp = int(input())
    arrN.append(temp)
    arrL.append([list(input()) for _ in range(temp)])
for cargo in range(n):
    noC = arrL[cargo]
    noH = arrN[cargo]
    print(noH, noC)
    yPoint = 0
    yCPoint = 0
    xPoint = 0
    for y in range(b - 1, -1, -1):
        for x in range(w):
            for yy in range(noH - 1, -1, -1):
                if noC[yy][x] == "X" and board[y][x] == "X":
                    print("break")
                    yCPoint = yy
                    break
            if yCPoint:
                break
        if yCPoint:
            break
    nH = noH - yCPoint + 1
    print(nH, noH, yCPoint, noH - yCPoint + 1)
    for cy in range(noH - 1, -1, -1):
        for cx in range(w):
            if noC[cy][cx] == "X":
                # print(nH + cy, cx)
                board[nH + cy][cx] = noC[cy][cx]
    print()
    for i in board:
        print(i)
    # for i in range()
