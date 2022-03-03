import sys

sys.stdin = open("Baekjoon16953.txt")

from collections import deque

A, B = map(int, input().split())
Q = deque([[A, 1]])
an = -1
while Q:
    now = Q.popleft()
    if now[0] == B:
        an = now[1]
        break
    a1 = int(str(now[0]) + "1")
    a2 = now[0] * 2
    if a1 <= B:
        Q.append([a1, now[1] + 1])
    if a2 <= B:
        Q.append([a2, now[1] + 1])
print(an)
