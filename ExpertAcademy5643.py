import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5643.txt")


def dfs(N):
    visited[N] += 1
    tempVisited[N] += 1
    # print(visited, root.get(N))
    if root.get(N):
        for f in root.get(N):
            # print(f)
            if tempVisited[f] == 0:
                dfs(f)


def dfsRev(N):
    visited[N] += 1
    tempVisitedRev[N] += 1
    # print(visited, root.get(N))
    if rootRev.get(N):
        for f in rootRev.get(N):
            # print(f)
            if tempVisitedRev[f] == 0:
                dfsRev(f)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())
    visited = [0] * (N + 1)
    root = {}
    rootRev = {}
    an = 0
    for i in range(M):
        a, b = map(int, input().split())
        root[a] = root.get(a, []) + [b]
        rootRev[b] = rootRev.get(b, []) + [a]
    for i in range(1, N + 1):
        # print("--", i)
        tempVisited = [0] * (N + 1)
        tempVisitedRev = [0] * (N + 1)
        dfs(i)
        dfsRev(i)
        print(i)
        print(tempVisited)
        print(tempVisitedRev)
        for g in range(1, N + 1):
            tempVisited[g] += tempVisitedRev[g]
            if tempVisited[g] == 0:
                break
            if g == N:
                an += 1

    # print(visited)
    print("#{} {}".format(tc, an))
