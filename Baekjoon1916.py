import sys

sys.stdin = open("Baekjoon1916.txt")
from collections import deque

N = int(input())
M = int(input())
tree = {}
minV = 1
for i in range(M):
    s, e, v = map(int, input().split())
    minV += v
    if tree.get(s) is None:
        tree[s] = {}
        tree[s][e] = v
    else:
        if tree[s].get(e) is not None:
            tree[s][e] = min(tree[s][e], v)
        else:
            tree[s][e] = v
S, E = map(int, input().split())
vi = [minV] * (N + 1)
vi[S] = 0
Q = deque([S])
while Q:
    now = Q.popleft()
    now_line = tree.get(now)
    if now_line:
        for t in now_line:
            f = now_line[t]
            if vi[t] > vi[now] + f:
                vi[t] = vi[now] + f
                Q.append(t)
print(vi[E])
