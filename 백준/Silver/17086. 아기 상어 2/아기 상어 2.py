from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque([])

for y in range(N):
    for x in range(M):
        if board[y][x]:
            Q.append([y, x])
dry = [-1, 1, -1, 1, -1, 1, 0, 0]
drx = [1, -1, -1, 1, 0, 0, 1, -1]
maxs = 0
while Q:
    ny, nx = Q.popleft()
    maxs = max(board[ny][nx], maxs)
    for d in range(8):
        wy = ny + dry[d]
        wx = nx + drx[d]
        if 0 <= wy < N and 0 <= wx < M and not board[wy][wx]:
            board[wy][wx] = board[ny][nx] + 1
            Q.append([wy, wx])

print(maxs - 1)