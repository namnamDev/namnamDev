import sys

sys.stdin = open("Baekjoon11866.txt")
from collections import deque

N, M = map(int, input().split())
Q = deque(list(range(1, N + 1)))
an = []
ad = "<"
while len(Q) > 1:
    for _ in range(M - 1):
        Q.append(Q.popleft())
    ad += str(Q.popleft()) + ", "
ad += str(Q.popleft()) + ">"
print(ad)
# print(N, M)
