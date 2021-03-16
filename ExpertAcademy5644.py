import sys
from collections import deque

sys.stdin = open("ExpertAcademy5644.txt")


def maxIdx(arrA, arrB):
    # print(arrA, arrB)
    mA = mB = 0
    maxAidx = maxBidx = 0
    re = 0
    # if len(arrA) and len(arrB):
    for i in arrA:
        if mA < BClist[i]:
            mA = BClist[i]
            maxAidx = i
    for i in arrB:
        if mB < BClist[i]:
            mB = BClist[i]
            maxBidx = i
    # print(mA, maxAidx, mB, maxBidx)

    if maxAidx == maxBidx:
        tempA = BClist[maxAidx]
        if len(arrA) > 1 and len(arrB) > 1:
            print(tempA, "-" * 20)
            arrA.pop(maxAidx)
            mA = maxIdx(arrA, arrB)

            arrB.pop(maxBidx)
            mB = maxIdx(arrA, arrB)
            aa = [tempA, mA, mB]
            re = max(aa)
    else:
        re = mA + mB
    # print(maxA, maxAidx, maxB, maxBidx)
    return re


SIZE = 10
dirs = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
for tc in range(int(input())):
    M, A = map(int, input().split())
    board = [[[]] * SIZE for _ in range(SIZE)]

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
        board[y][x] = [i]
        dfsboard[y][x] = 1
        # print(c)
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
                            if len(board[wy][wx]) != 0:
                                board[wy][wx].append(i)
                            else:
                                board[wy][wx] = [i]
        # for ff in dfsboard:
        #     print(ff)
    an = 0

    for i in range(M):
        Anow[0] += dirs[Amove[i]][0]
        Anow[1] += dirs[Amove[i]][1]
        Bnow[0] += dirs[Bmove[i]][0]
        Bnow[1] += dirs[Bmove[i]][1]
        tempA = []
        tempB = []
        maxAidx = 0
        maxBidx = 0
        tempA = board[Anow[0]][Anow[1]]
        tempB = board[Bnow[0]][Bnow[1]]

        an += maxIdx(tempA, tempB)
        print(an)

    print("#{} {}".format(tc + 1, an))
    # print(board)
# 1 1200
# 2 3290
# 3 16620
# 4 40650
# 5 52710
