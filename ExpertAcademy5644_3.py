import sys
from collections import deque

sys.stdin = open("ExpertAcademy5644.txt")


def maxIdx(arrA, arrB):
    mA = mB = 0
    maxAidx = maxBidx = 0
    Aidx = Bidx = 0
    for i in range(len(arrA)):
        if mA < BClist[arrA[i]]:
            mA = BClist[arrA[i]]
            maxAidx = arrA[i]
            Aidx = i
    for f in range(len(arrB)):
        if mB < BClist[arrB[f]]:
            mB = BClist[arrB[f]]
            maxBidx = arrB[f]
            Bidx = f

    if maxAidx == maxBidx and maxAidx != 0:
        tempA = BClist[maxAidx]
        tempaa = arrA.pop(Aidx)
        mA = maxIdx(arrA, arrB)
        arrA.append(tempaa)
        arrB.pop(Bidx)
        mB = maxIdx(arrA, arrB)
        aa = [tempA, mA, mB]
        return max(aa)

    re = mA + mB
    return re


SIZE = 10
dirs = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
for tc in range(int(input())):
    M, A = map(int, input().split())
    board = [[0] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for g in range(SIZE):
            board[i][g] = [0]
    Amove, Bmove = list(map(int, input().split())), list(map(int, input().split()))
    Anow, Bnow = [0, 0], [9, 9]
    BClist = [0] * (A + 1)
    for i in range(A):
        dfsboard = [[0] * SIZE for _ in range(SIZE)]
        x, y, c, p = map(int, input().split())
        y -= 1
        x -= 1
        BClist[i + 1] = p
        Q = deque([[y, x]])
        board[y][x].append(i + 1)
        dfsboard[y][x] = 1
        while len(Q):
            yy, xx = map(int, Q.popleft())
            if dfsboard[yy][xx] <= c:
                for f in range(1, 5):
                    wy = yy + dirs[f][0]
                    wx = xx + dirs[f][1]
                    if 0 <= wy < SIZE and 0 <= wx < SIZE:
                        if dfsboard[wy][wx] == 0:
                            dfsboard[wy][wx] = dfsboard[yy][xx] + 1
                            Q.append([wy, wx])
                            board[wy][wx].append(i + 1)

    cnt = 0
    tempA = board[Anow[0]][Anow[1]]
    tempB = board[Bnow[0]][Bnow[1]]
    an = maxIdx(tempA, tempB)
    for i in range(M):
        Anow[0] += dirs[Amove[i]][0]
        Anow[1] += dirs[Amove[i]][1]
        Bnow[0] += dirs[Bmove[i]][0]
        Bnow[1] += dirs[Bmove[i]][1]

        tempA = board[Anow[0]][Anow[1]]
        tempB = board[Bnow[0]][Bnow[1]]

        cnt += 1
        TEST = maxIdx(tempA, tempB)
        an += TEST

    print("#{} {}".format(tc + 1, an))
    # print(board)
# 1 1200
# 2 3290
# 3 16620
# 4 40650
# 5 52710
