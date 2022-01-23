import sys

sys.stdin = open('Baekjoon2580.txt')

from collections import deque

board = [list(map(int, input().split())) for _ in range(9)]


def se(paY):
    sums = 0
    vi = [0] * 9
    for i in board[paY]:
        sums += i
        if i:
            vi[i - 1] += 1
    # print("se", vi.count(0), 45 - sums)
    # print(vi)
    if vi.count(0) > 1:
        return 0
    return 45 - sums


def ga(paX):
    sums = 0
    vi = [0] * 9
    for i in range(9):
        sums += board[i][paX]
        if board[i][paX]:
            vi[board[i][paX] - 1] += 1
    # print("ga", vi.count(0), 45 - sums)
    if vi.count(0) > 1:
        return 0
    return 45 - sums


def sa(paY, paX):
    minY = (paY // 3) * 3
    minX = (paX // 3) * 3
    sums = 0
    vi = [0] * 9
    for y in range(minY, minY + 3):
        for x in range(minX, minX + 3):
            sums += board[y][x]
            # print(y, x, board[y][x])
            if board[y][x]:
                vi[board[y][x] - 1] += 1
    if vi.count(0) > 1:
        return 0
    return 45 - sums


nonList = deque([])
for y in range(9):
    for x in range(9):
        if not board[y][x]:
            tempNum = max(sa(y, x), ga(x), se(y))
            if tempNum:
                board[y][x] = tempNum
            else:
                nonList.append([y, x])
while nonList:
    now = nonList.popleft()
    y, x = now[0], now[1]
    tempNum = max(sa(y, x), ga(x), se(y))
    if tempNum:
        board[y][x] = tempNum
    else:
        nonList.append([y, x])

for i in board:
    print(*i)

# vii = [0] * 10
#
# for i in board:
#     for x in i:
#         vii[x] += 1
# print(vii)
