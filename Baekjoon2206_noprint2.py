import sys
from collections import deque

sys.stdin = open('Baekjoon2206.txt')

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0, 0] * M for _ in range(N)]

Q = deque([[0, 0]])
visited[0][0] = 1
while len(Q):
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    break_wall = 0
    break_point = []
    an = N * M
    re = []
    while len(Q):
        now = Q.popleft()
        if visited[N - 1][M - 1]:
            re.append(visited[N - 1][M - 1])
            break
        for i in range(4):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < N and 0 <= wx < M:
                if not visited[wy][wx]:
                    if board[wy][wx]:
                        if not break_wall:
                            print("break")
                            visited[wy][wx] = 1 + visited[now[0]][now[1]]
                            Q.append([wy, wx])
                            break_wall += 1
                            break_point = [wy, wx]
                    else:
                        visited[wy][wx] = 1 + visited[now[0]][now[1]]
                        Q.append([wy, wx])

    print()
    if break_wall:
        board[break_point[0]][break_point[1]] = 1
        Q = deque([[0, 0]])
    for i in visited:
        print(i)

# an = -1 if not visited[N - 1][M - 1] else visited[N - 1][M - 1]

# for i in visited:
#     print(i)
print(break_point)
print(an, visited[N - 1][M - 1])
