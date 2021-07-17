import sys

sys.stdin = open('Baekjoon2606.txt')
from collections import deque

N = int(input())
M = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1
vi = [0] * (N + 1)
Q = deque([1])
vi[1] = 1
cnt = 0
while Q:
    now = Q.popleft()
    line = board[now]
    for i in range(1, N + 1):
        if line[i] and not vi[i]:
            vi[i] = 1
            Q.append(i)
            cnt += 1

print(cnt)
