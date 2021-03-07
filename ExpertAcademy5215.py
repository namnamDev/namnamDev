import sys

sys.stdin = open("ExpertAcademy5215.txt")


def dfs(start, kal, li):
    global an
    sums = 0
    if kal > M or len(li) > N:
        return
    else:
        for i in li:
            sums += arr[i][0]
        an.append(sums)
        for i in range(start, N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, kal + arr[i][1], li + [i])
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    an = []
    dfs(0, 0, [])
    print("#{} {}".format(tc, max(an)))
