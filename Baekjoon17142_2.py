import sys

sys.stdin = open("Baekjoon17142.txt")

from collections import deque


def cho(paArr, idx):
    if len(paArr) == M:
        global choList
        choList.append(paArr)
        return
    for i in range(idx, len(bList)):
        cho(paArr + [i], i + 1)


def che(paArr):
    res = 0
    for y in range(N):
        for x in range(N):
            if not paArr[y][x] and not board[y][x]:
                return -1
            else:
                res = max(res, paArr[y][x])
    return res


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
bList = []
anList = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 2:
            bList.append([y, x])
choList = []
cho([], 0)
# print(choList)
for chOne in choList:
    vi = [[0] * N for _ in range(N)]
    Q = deque([])
    for i in chOne:
        vi[bList[i][0]][bList[i][1]] = 1
        Q.append(bList[i])
    print(Q)
    while Q:
        now = Q.popleft()
        for d in range(4):
            wy = dy[d] + now[0]
            wx = dx[d] + now[1]
            if 0 <= wy < N and 0 <= wx < N and not vi[wy][wx]:
                if board[wy][wx] != 1:
                    vi[wy][wx] = vi[now[0]][now[1]] + 1
                    Q.append([wy, wx])

    for i in vi:
        print(i)
    tempAn = che(vi)
    print("now", tempAn)
    if 0 < tempAn:
        anList.append(tempAn)
print(anList)
print(min(anList) - 1)
