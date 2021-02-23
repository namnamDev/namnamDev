import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5643.txt")


# 특정한 학생 s 에 대해서,
# 어떤 학생들이 내 경로 위에 있고,
# 그 학생들을 제외한 모든 학생들의 경로 위에 s가 있다면,
# 모든 순서가 파악되기 때문에 s의 키 순위를 알 수 있다.
# 따라서 개별 학생에 대해서 dfs를 통해서 visited를 작성하고,
# visited를 대각선으로 데칼코마니


def dfs(v, M):
    visited[v] = 1

    for w in range(N + 1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w, M)


for t in range(int(input())):
    N = int(input())
    M = int(input())

    adj = [[0] * (N + 1) for n in range(N + 1)]

    for m in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1

    arr = []

    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        dfs(i, M)
        arr.append(visited)

    for r in range(N):
        arr[r].pop(0)

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                arr[c][r] = 1

    ans = 0
    for r in range(N):
        if sum(arr[r]) == N:
            ans += 1

    print('#{} {}'.format(t + 1, ans))
