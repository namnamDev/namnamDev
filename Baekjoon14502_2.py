import sys

sys.stdin = open('Baekjoon14502.txt')

from collections import deque

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]


def copyB(anArr):
    tempArr = [[0] * M for _ in range(N)]
    for i in range(N):
        for g in range(M):
            tempArr[i][g] = anArr[i][g]
    return tempArr


def counting2(arr):
    pBoard = copyB(arr)
    cnt = 0
    Q = deque()
    for ii in range(len(birus)):
        Q.append(birus[ii])
    while Q:
        now = Q.popleft()
        for d in range(4):
            wy = now[0] + diry[d]
            wx = now[1] + dirx[d]
            if 0 <= wy < N and 0 <= wx < M and not pBoard[wy][wx]:
                cnt += 1
                pBoard[wy][wx] = 2
                Q.append([wy, wx])
    return [pBoard, cnt]


def backt(arr, cntW):
    if cntW == 3:
        global minB
        global aaa
        res = counting2(arr)
        if res[1] < minB:
            minB = res[1]
            aaa = res[0]
        return
    tempArr = copyB(arr)
    for i in range(N):
        for g in range(M):
            if not tempArr[i][g]:
                tempArr[i][g] = 1
                backt(tempArr, cntW + 1)
                tempArr[i][g] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
birus = []
minB = N * M
aaa = []
total = 0
for f in range(N):
    for g in range(M):
        if board[f][g] == 2:
            birus.append([f, g])

backt(board, 0)
for i in aaa:
    for g in i:
        if not g:
            total += 1
print(total)
