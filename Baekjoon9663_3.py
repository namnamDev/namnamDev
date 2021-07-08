def dfs(y):
    if y == N:
        return
    for x in range(N):
        if not vi[x] and not viL[y + x] and not viL[y + N - 1 - x]:
            vi[x] = 1
            viL[y + x] = 1
            viL[y + N - 1 - x] = 1
            dfs(y + 1)


# N=6 00 viL[y+x] viR[y+N-x]
# x=4 y=1 viL[2] viR[11]
# x=4 y=4 viL[5] viR[3]
# x=0 y=5 viL[11] viR[0]
# x=1 y=0 viL[4 = N-1-x] viR[1]
# x=1 y=1 viL[5 = N-1-x+y] viR[2]
# x=1 y=2 viL[6 = N-1-x+y] viR[3 = y+x]
# x=3 y=4 viL[6] viR[7]
N = int(input())
cnt = 0
used = []

# board = [[0] * N for _ in range(N)]
vi = [0] * N
viL = [0] * (2 * N - 1)
viR = [0] * (2 * N - 1)
dfs(0)

print(cnt)
