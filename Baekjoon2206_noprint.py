import sys
from collections import deque

sys.stdin = open('Baekjoon2206.txt')

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

visited[0][0] = 1
flag = [N - 1, M - 1]
Q = deque([[0, 0]])
reached_walls = []
re = []
while len(Q):
    if visited[N - 1][M - 1]:
        re.append(visited[N - 1][M - 1])
        break
    now = Q.popleft()
    for i in range(4):
        wy = now[0] + diry[i]
        wx = now[1] + dirx[i]
        if 0 <= wy < N and 0 <= wx < M:
            if not visited[wy][wx]:
                visited[wy][wx] = 1 + visited[now[0]][now[1]]
                if board[wy][wx]:
                    reached_walls.append([wy, wx])
                else:
                    Q.append([wy, wx])

for wall in reached_walls:
    print(wall)
    Q = deque([[0, 0]])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    board[wall[0]][wall[1]] = 0
    temp_an = 0
    while len(Q):
        if visited[N - 1][M - 1]:
            re.append(visited[N - 1][M - 1])
            break
        now = Q.popleft()
        for i in range(4):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < N and 0 <= wx < M:
                if not visited[wy][wx]:
                    if not board[wy][wx]:
                        visited[wy][wx] = 1 + visited[now[0]][now[1]]
                        Q.append([wy, wx])
    board[wall[0]][wall[1]] = 1

an = -1 if not re else min(re)
print(an)
