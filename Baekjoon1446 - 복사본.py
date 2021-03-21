import sys
from collections import deque

sys.stdin = open("Baekjoon1446.txt")


def dfs(now, length, used):
    if used:
        if len(used) == len(spot):
            return

    arr = spot.get(now)

    for i in range(len(arr)):
        if arr[i][0] not in used:
            dfs(now + 1, length + arr[i][1], used + [arr[i][0]])


N, D = map(int, input().split())
spot = [[0] * 10000 for _ in range(10000)]
for i in range(N):
    start, end, length = map(int, input().split())
    spot[start][end] = length
    # visited = list(spot)
print(spot)
# print(used)

for i in spot:
    dfs(i, 0, [])
