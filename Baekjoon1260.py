import sys

sys.stdin = open('Baekjoon1260.txt')
from collections import deque


def dfs(idx, arr):
    global dfsArr
    line = board[idx]
    for i in range(N + 1):
        if line[i] and not vidfs[i]:
            dfsArr.append(i)
            vidfs[i] = 1
            dfs(i, arr + [i])


N, M, V = map(int, input().split())
board = [[0] * (N + 1) for _ in range(N + 1)]
vibfs = [0] * (N + 1)
vidfs = [0] * (N + 1)
for i in range(M):
    s, e = map(int, input().split())
    board[s][e] = 1
    board[e][s] = 1

Qbfs = deque([V])
Qdfs = [V]
vibfs[V] = 1
vidfs[V] = 1
bfsArr = [V]
dfsArr = [V]

while len(Qbfs):
    nowbfs = Qbfs.popleft()
    for i in range(1, N + 1):
        if board[nowbfs][i] and not vibfs[i]:
            vibfs[i] = 1
            Qbfs.append(i)
            bfsArr.append(i)
dfs(V, [])
print(*dfsArr)
print(*bfsArr)
# andfs = ''
# anbfs = ''
# for i in dfsArr:
#     andfs += str(i) + ' '
# for g in bfsArr:
#     anbfs += ' ' + str(g)
# print(andfs)
# print(anbfs)
