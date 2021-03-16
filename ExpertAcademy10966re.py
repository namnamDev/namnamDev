import sys

from collections import deque

sys.stdin = open("ExpertAcademy10966.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = deque()
    for i in range(N):
        for g in range(M):
            if board[i][g] == 'W':
                visited[i][g] = 1
                Q.append([i, g])

    while len(Q):
        y, x = Q.popleft()
        for i in range(4):
            wy = x + diry[i]
            wx = y + dirx[i]
            if 0 <= wy < N and 0 <= wx < M:
                if visited[wy][wx] == 0:
                    visited[wy][wx] = visited[y][x] + 1
                    Q.append([wy, wx])

    cnt = 0
    for i in visited:
        cnt += sum(i)
    cnt -= N * M

    print("#{} {}".format(tc + 1, cnt))
