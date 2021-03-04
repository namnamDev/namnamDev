import sys

sys.stdin = open("Baekjoon1168.txt")


def dfs(start):
    global visited
    global cnt
    visited[start] = 1
    if 1 not in board[start]:
        cnt += 1
        return
    else:
        for i in range(N):
            if board[start][i] and visited[i] == 0:
                dfs(i)


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
visited = [0] * N
visited[M] = 1
board = [[0] * N for _ in range(N)]
start = []
cnt = 0
for i in range(N):
    if arr[i] == -1:
        start.append(i)
    else:
        if arr[i] != M and i != M:
            board[arr[i]][i] = 1

for i in range(len(start)):
    if start[i] != M:
        dfs(start[i])
print(cnt)
