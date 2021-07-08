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
            print()
            for i in tempArr:
                print(i)
            used.append(tempArr)
        return
    if y == N:
        return
    for xx in range(x, N):
        if not arr[y][xx]:
            arr[y][xx] = 2
            for i in range(8):
                wy = y + diry[i]
                wx = xx + dirx[i]
                while 0 <= wy < N and 0 <= wx < N:
                    arr[wy][wx] = 1
                    wy += diry[i]
                    wx += dirx[i]
            dfs(y + 1, 0, arr, M + 1)  # 퀸 놓고 넘기기. 해당 열에는 퀸을 놓을수 없으므로 y+1해주고, x=0
            dfs(y, xx + 1, tempArr, M)  # 퀸 놓지않고 넘기기


N = int(input())
cnt = 0
used = []

board = [[0] * N for _ in range(N)]
dfs(0, 0, board, 0)
print(cnt)
