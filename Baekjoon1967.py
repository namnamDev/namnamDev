import sys

sys.stdin = open("Baekjoon1967.txt")
from collections import deque

N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    y, x, v = map(int, input().split())
    arr[y].append([x, v])
    arr[x].append([y, v])
maxs = 0
for i in range(1, N + 1):
    vi = [0] * (N + 1)
    vi[i] = 1
    stack = deque([i])
    while stack:
        now = stack.pop()
        now_line = arr[now]
        for y, v in now_line:
            if not vi[y]:
                vi[y] = vi[now] + v
                stack.append(y)
    maxs = max(maxs, max(vi) - 1)
print(maxs)
