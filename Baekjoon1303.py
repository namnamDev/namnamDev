import sys

sys.stdin = open("Baekjoon1303.txt")


def dfs(y, x, word):
    global visited
    global cnt
    cnt += 1
    visited[y][x] = 1
    for i in range(4):
        wy = y + diry[i]
        wx = x + dirx[i]
        if 0 <= wy < M and 0 <= wx < N:
            if board[wy][wx] == word and visited[wy][wx] == 0:
                dfs(wy, wx, word)


diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
wli = bli = 0
for i in range(M):
    for g in range(N):
        if visited[i][g] == 0:
            cnt = 0
            if board[i][g] == 'W':
                dfs(i, g, 'W')
                wli += cnt ** 2
            else:
                dfs(i, g, 'B')
                bli += cnt ** 2
            cnt = 0
print(wli, bli)
