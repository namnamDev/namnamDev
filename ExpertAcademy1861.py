import sys

sys.stdin = open("ExpertAcademy1861.txt")


def dfs(idx):
    temp = arr[idx[0]][idx[1]]
    for drs in range(4):
        wy = idx[0] + diry[drs]
        wx = idx[1] + dirx[drs]
        if 0 <= wy < N and 0 <= wx < N and not visitied[wy][wx]:
            if arr[wy][wx] == temp + 1:
                visitied[wy][wx] = visitied[idx[0]][idx[1]] + 1
                dfs([wy, wx])
                return

    if visitied[idx[0]][idx[1]] > 1:
        global res
        res.append([visitied[idx[0]][idx[1]], arr[idx[0]][idx[1]]])


diry = [1, -1, 0, 0]
dirx = [0, 0, 1, -1]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    res = []
    visitied = [[0] * N for _ in range(N)]
    print(tc + 1)
    for i in range(N):
        for g in range(N):
            visitied[i][g]
            dfs([i, g])
    for i in visitied:
        print(i)
    print(res)
