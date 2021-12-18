import sys

sys.stdin = open('Baekjoon2583.txt')

from collections import deque

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for i in range(K):
    m1, n1, m2, n2 = map(int, input().split())
    for x in range(m1, m2):
        for y in range(n1, n2):
            board[y][x] += 1
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
answers = []
for yy in range(N):
    for xx in range(M):
        if board[yy][xx] == 0:
            cnt = 1
            Q = deque([[yy, xx]])
            board[yy][xx] = -1
            while Q:
                now = Q.popleft()
                for dirs in range(4):
                    wy = now[0] + diry[dirs]
                    wx = now[1] + dirx[dirs]
                    if 0 <= wy < N and 0 <= wx < M and board[wy][wx] == 0:
                        board[wy][wx] = -1
                        Q.append([wy, wx])
                        cnt += 1
            answers.append(cnt)
print(len(answers))
print(*sorted(answers))
