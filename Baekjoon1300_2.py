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

cnt = 0
visited[0][0] = 1
minis = arr[N - 1][N - 1]
Q = [[0, 0]]
while cnt < k:
    now = Q.pop(0)
    for i in range(4):
        wy = now[0] + diry[i]
        wx = now[1] + dirx[i]
        if 0 <= wy < N and 0 <= wx < N:
            if visited[wy][wx] == 0:
                Q.append([wy, wx])
                visited[wy][wx] = 1
    cnt += 1
    print(Q)
print(minis)
for i in arr:
    print(i)
