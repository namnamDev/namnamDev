import sys

sys.stdin = open("Baekjoon1238.txt")

from collections import deque

N, M, X = map(int, input().split())
board = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    board[s].append([e, v])
max_v = 0
vi = [100 * 1000] * (N + 1)
Q = deque([X])
vi[0] = 0
vi[X] = 0
while Q:
    n = Q.popleft()
    temp_line = board[n]
    for d, v in temp_line:
        if vi[d] > vi[n] + v:
            vi[d] = vi[n] + v
            Q.append(d)
for i in range(1, N + 1):
    Q = deque([i])
    vi2 = [100 * 1000] * (N + 1)
    vi2[0] = 0
    vi2[i] = 0
    while Q:
        n = Q.popleft()
        temp_line = board[n]
        for d, v in temp_line:
            if vi2[d] > vi2[n] + v:
                vi2[d] = vi2[n] + v
                Q.append(d)
    go = vi2[X]
    max_v = max(max_v, vi2[X] + vi[i])
print(max_v)
