import sys
from collections import deque

sys.stdin = open('ExpertAcademy1249.txt')
dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]
INF = 999999999

for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    keys = [[INF] * N for _ in range(N)]
    keys[0][0] = 0

    Q = deque([[0, 0]])
    while len(Q):
        now = Q.popleft()
        y = now[0]
        x = now[1]
        for drs in range(4):
            wy = y + dry[drs]
            wx = x + drx[drs]
            if 0 <= wy < N and 0 <= wx < N:
                if keys[y][x] + board[wy][wx] < keys[wy][wx]:
                    keys[wy][wx] = keys[y][x] + board[wy][wx]
                    Q.append([wy, wx])
    an = keys[N - 1][N - 1]
    print("#{} {}".format(tc + 1, an))
