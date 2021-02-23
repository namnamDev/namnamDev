import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5643.txt")


def dfs(start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        visited.add(node)
        edges = graph[node]
        for edge in edges:
            if edge not in visited:
                stack.append(edge)
                counts[start][edge] = True
                counts[node][edge] = True


def check(i):
    for j in range(1, N + 1):
        if i == j:
            continue
        if counts[i][j] == False and counts[j][i] == False:
            return False
    return True


T = int(input())
for t in range(T):
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N + 1)]
    counts = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = list(map(int, input().split()))
        graph[a].append(b)

    for i in range(1, N + 1):
        dfs(i)

    ans = 0
    for i in range(1, N + 1):
        if check(i):
            ans += 1

    print("#{} {}".format(t + 1, ans))
