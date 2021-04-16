import sys
import time

sys.stdin = open('Baekjoon2580.txt')
start = time.time()
from collections import deque


def count9(arr, point):
    re = []
    if board[point[0]][point[1]]:
        return
    for i in range(1, 10):
        if i not in arr:
            re.append(i)
    if len(re) == 1:
        board[point[0]][point[1]] = re[0]
    return re


board = [list(map(int, input().split())) for _ in range(9)]

Q = deque([])
for i in range(9):
    for g in range(9):
        if not board[i][g]:
            Q.append([i, g])
while len(Q):
    i = Q.popleft()
    if not board[i[0]][i[1]]:
        row = board[i[0]]
        count9(row, i)
        col = []
        box = []
        for g in range(9):
            col.append(board[g][i[1]])
        count9(col, i)
        boxy = (i[0] // 3) * 3
        boxx = (i[1] // 3) * 3
        for f in range(3):
            templine = board[boxy + f]
            box += templine[boxx:boxx + 3]
        count9(box, i)

        if not board[i[0]][i[1]]:
            Q.append(i)

for i in board:
    print(*i)
print((time.time() - start) * 1000)
