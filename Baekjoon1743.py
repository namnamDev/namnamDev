import sys

sys.stdin = open("Baekjoon1743.txt")

from collections import deque

N, M, K = map(int, input().split())
board = [[0] * (M + 1) for _ in range(N + 1)]
vi = [[0] * (M + 1) for _ in range(N + 1)]
diry = [0, 0, - 1, 1]
dirx = [1, -1, 0, 0]
for i in range(K):
    y, x = map(int, input().split())
    board[y][x] = 1
answer = []
for y in range(1, N + 1):
    for x in range(1, M + 1):
        if board[y][x] and not vi[y][x]:
            Q = deque([[y, x]])
            vi[y][x] = 1
            cnt = 1
            while Q:
                now = Q.popleft()
                for dirs in range(4):
                    wy = now[0] + diry[dirs]
                    wx = now[1] + dirx[dirs]
                    if 1 <= wy < N + 1 and 1 <= wx < M + 1 and board[wy][wx] and not vi[wy][wx]:
                        vi[wy][wx] = 1
                        Q.append([wy, wx])
                        cnt += 1
            answer.append(cnt)
print(max(answer))
