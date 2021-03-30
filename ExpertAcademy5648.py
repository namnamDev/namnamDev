import sys
from collections import deque

sys.stdin = open('ExpertAcademy5648.txt')
diry = [1, -1, 0, 0]
dirx = [0, 0, -1, 1]
SIZE = 2000
for tc in range(int(input())):
    N = int(input())
    board = [[0] * SIZE for _ in range(SIZE)]
    Q = deque()
    memo = []
    for i in range(N):
        x, y, dirs, k = map(int, input().split())
        x += 1000
        y += 1000
        Q.append([x, y, dirs, k])
    an = 0
    while len(Q):
        temp = Q
        Q = deque()
        while len(temp):
            nx, ny, dirs, k = map(int, temp.popleft())
            wx = nx + dirx[dirs]
            wy = ny + diry[dirs]
            if 0 <= wx < SIZE and 0 <= wy < SIZE:
                appendornot = True
                for g in range(len(Q)):
                    if Q[g][0] == wx and Q[g][1] == wy:
                        an += Q[g][3] + k
                        Q[g] = [-20000, -20000, 0, 0]
                        appendornot = False
                        break
                if appendornot:
                    Q.append([wx, wy, dirs, k])

    print("#{} {}".format(tc + 1, an))
