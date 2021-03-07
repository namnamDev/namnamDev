import sys

sys.stdin = open("ExpertAcademy5215.txt")


def dfs(start, kal, yamy, cnt):
    global an
    sums = 0
    if kal > M or cnt > N:
        return
    else:
        if an < yamy:
            an = yamy
        for i in range(start, N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, kal + arr[i][1], yamy + arr[i][0], cnt + 1)
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    an = 0
    dfs(0, 0, 0, 0)
    print("#{} {}".format(tc, an))
