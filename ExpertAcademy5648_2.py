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
        print('start', temp, Q)
        while len(temp):
            aaq = temp.popleft()
            if len(aaq) > 1:
                nx, ny, dirs, k = map(int, aaq)
                wx = nx + dirx[dirs]
                wy = ny + diry[dirs]
                if 0 <= wx < SIZE and 0 <= wy < SIZE:
                    Q.append([wx, wy, dirs, k])
                    appendornot = True

        for g in range(len(Q)):
            if len(Q[g]) > 1:
                tempx, tempy = Q[g][0], Q[g][1]
                continuBol = False
                for i in range(g + 1, len(Q)):
                    if len(Q[i]) > 1:
                        if Q[i][0] == tempx and Q[i][1] == tempy:
                            an += Q[g][3] + Q[i][3]
                            Q[g] = [0]
                            Q[i] = [0]

                            continuBol = True
                            break
                if continuBol:
                    break
        print('end', temp, Q)
    print("#{} {}".format(tc + 1, an))
