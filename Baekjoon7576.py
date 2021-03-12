import sys
from collections import deque

sys.stdin = open("Baekjoon7576.txt")
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
temp = deque()
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            Q.append([n, m])

cnt = -1
while len(Q) != 0:
    temp = deque()
    while len(Q) != 0:
        now = Q.popleft()
        for i in range(4):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < N and 0 <= wx < M:
                if board[wy][wx] == 0:
                    board[wy][wx] = 1
                    temp.append([wy, wx])
    cnt += 1
    Q = deque(temp)
for n in board:
    if 0 in n:
        cnt = -1
        break

print(cnt)
