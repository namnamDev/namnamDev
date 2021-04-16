import sys

sys.stdin = open('Baekjoon1753.txt')


def dfs(value, start):
    global maxs
    if visited[idx]:
        return
    if value > maxs:
        return
    templine = board[start]

    for g in range(V):
        if templine[g]:
            if visited[g] == 0:
                visited[g] = value + templine[g]
            else:
                if visited[g] > value + templine[g]:
                    visited[g] = value + templine[g]
            dfs(visited[g], g)


V, E = map(int, input().split())
start = int(input())
board = [[0] * V for _ in range(V)]
maxs = 0
for i in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    maxs += w
    if 0 < board[u][v]:
        if board[u][v] > w:
            board[u][v] = w
    else:
        board[u][v] = w

for i in range(V):
    visited = [0] * V
    visited[start - 1] = 1
    idx = i
    dfs(0, start - 1)

for i in range(V):
    if visited[i]:
        if i == start - 1:
            print(0)
        else:
            print(visited[i])
    else:
        print('INF')
