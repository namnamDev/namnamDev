import sys

sys.stdin = open("Baekjoon12852.txt")
from collections import deque

n = int(input())
Q = deque([[n, []]])
used = {}

while Q:
    x, y = Q.popleft()
    if x == 1:
        print(len(y))
        print(n, *y)
        break
    t = []
    if not x % 3:
        t.append(x // 3)
    if not x % 2:
        t.append(x // 2)
    if x > 1:
        t.append(x - 1)
    for tt in t:
        if not used.get(tt):
            used[tt] = 1
            Q.append([tt, y + [tt]])
