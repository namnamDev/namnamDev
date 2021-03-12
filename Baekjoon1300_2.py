def dfs(cnt, y, x):
    global mins
    if cnt == k:
        if mins > arr[y][x]:
            mins = arr[y][x]
        return

    for i in range(4):
        wy = y + diry[i]
        wx = x + dirx[i]
        if 0 <= wy < N and 0 <= wx < N:
            if visited[wy][wx] == 0:
                visited[wy][wx] = 1
                dfs(cnt + 1, wy, wx)
                # visited[wy][wx] = 0


diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
N = int(input())
k = int(input())
arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
B = [0] * N ** 2
for i in range(N):
    for g in range(N):
        arr[i][g] = (i + 1) * (g + 1)

# now = [0, 0]
visited[0][0] = 1
mins = arr[N - 1][N - 1]
for i in arr:
    print(i)
dfs(0, 0, 0)
print(mins)
