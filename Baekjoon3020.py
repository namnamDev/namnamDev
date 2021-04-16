import sys
from collections import deque

sys.stdin = open('Baekjoon3020.txt')
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
fly = [0] * M
for i in range(0, N, 2):
    h = arr[i]
    for g in range(h):
        fly[g] += 1
    h2 = arr[i + 1]
    for g in range(M - 1, h2 - 2, -1):
        fly[g] += 1
print(min(fly), fly.count(min(fly)))
