import sys

sys.stdin = open('Baekjoon2644.txt')
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
arrSons = [[] for _ in range(n + 1)]
arrParent = [0] * (n + 1)
vi = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    arrSons[x].append(y)
    arrParent[y] = x

Q = deque([a])
vi[a] = 1
while Q:
    now = Q.popleft()
    if now:
        nowSons = arrSons[now]
        nowParent = arrParent[now]

        if not vi[nowParent] and nowParent:
            vi[nowParent] = vi[now] + 1
            Q.append(nowParent)

        for i in range(len(nowSons)):
            if not vi[nowSons[i]]:
                Q.append(nowSons[i])
                vi[nowSons[i]] = vi[now] + 1

print(vi[b] - 1)
