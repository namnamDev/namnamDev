import sys

sys.stdin = open('Baekjoon2211.txt')

from collections import deque


def my_function(idx):
    vi[idx] = 1
    min_val = INF
    min_idx = 0
    temp = board[idx]
    tempQ = []
    for i in range(N):
        if not vi[i]:
            tempQ.append([temp[i], i])
    tempQ.sort()
    print(tempQ)
    while len(tempQ):
        now = tempQ.pop(0)
        vi[now[0]] = 1
        if now[1] < vals[now[0]]:
            vals[now[0]] = now[1]
        
    # if temp[i] < min_val and not vi[i]:
    #     min_val = temp[i]
    #     min_idx = i


INF = 9999999999
N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, val = map(int, input().split())
    board[a - 1][b - 1] = val
    board[b - 1][a - 1] = val
for i in board:
    print(i)
vi = [0] * N
vals = [INF] * N
vals[0] = 0
vi[0] = 1
my_function(0)
