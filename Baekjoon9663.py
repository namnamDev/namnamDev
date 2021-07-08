import sys

# sys.stdin = 8

diry = [-1, 1, 0, 0, -1, 1, 1, -1]
dirx = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(y, x, arr, M):
    tempArr = [[0] * N for _ in range(N)]
    for i in range(N):
        for g in range(N):
            tempArr[i][g] = arr[i][g]  # 카피
    if M == N:
        if tempArr not in used:
            global cnt
            cnt += 1
            used.append(tempArr)
        return
    if y == N:
        return
    for yy in range(y, N):
        for xx in range(x, N):
            if not arr[yy][xx]:
                arr[yy][xx] = 2
                for i in range(8):
                    wy = yy + diry[i]
                    wx = xx + dirx[i]
                    while 0 <= wy < N and 0 <= wx < N:
                        arr[wy][wx] = 1
                        wy += diry[i]
                        wx += dirx[i]
                print(yy, xx)
                for i in arr:
                    print(i)
                dfs(yy + 1, 0, arr, M + 1)
                dfs(yy, xx + 1, tempArr, M)


N = 4
cnt = 0
used = []
board = [[0] * N for _ in range(N)]
dfs(0, 0, board, 0)
print(len(used), cnt)
