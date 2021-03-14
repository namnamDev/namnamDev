import sys
from collections import deque

sys.stdin = open("Baekjoon2178.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
flag = [N - 1, M - 1]
Q = deque([[0, 0]])
visited[0][0] = 1
while len(Q) != 0:
    now = Q.popleft()
    if visited[N - 1][M - 1]:
        print(visited[N - 1][M - 1])
        break
    else:
        for i in range(4):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < N and 0 <= wx < M:
                if arr[wy][wx] and not visited[wy][wx]:
                    Q.append([wy, wx])
                    visited[wy][wx] = 1 + visited[now[0]][now[1]]
