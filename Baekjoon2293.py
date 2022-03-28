import sys

sys.stdin = open("Baekjoon2293.txt")
from collections import deque

a, b = map(int, input().split())
coins = []
for i in range(a):
    coins.append(int(input()))
Q = deque([[0]])
cnt = 0
while Q:
    now = Q.popleft()
    # print(Q)
    if sum(now) < b:
        for c in coins:
            if now[-1] <= c:
                Q.append(now + [c])
    elif sum(now) == b:
        cnt += 1
print(cnt)
