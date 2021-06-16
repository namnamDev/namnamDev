import sys
from collections import deque

sys.stdin = open('Baekjoon1926.txt')
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
maxCnt = 0
pics = 0
vi = [[0] * M for _ in range(N)]

for i in range(N):
    for g in range(M):
        if board[i][g] and not vi[i][g]:
            # vi[i][g] = 1
            pics += 1
            cnt = 0
            Q = [[i, g]]
            while len(Q):
                now = Q.pop()
                cnt += 1
                vi[now[0]][now[1]] = 1
                for f in range(4):
                    wy = now[0] + diry[f]
                    wx = now[1] + dirx[f]
                    if 0 <= wy < N and 0 <= wx < M and board[wy][wx] and not vi[wy][wx]:
                        vi[wy][wx] = 1
                        Q.append([wy, wx])

            maxCnt = max(maxCnt, cnt)
print(pics)
print(maxCnt)
