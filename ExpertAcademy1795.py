import sys
from collections import deque

sys.stdin = open('ExpertAcademy1795.txt')


def dik(idx):
    min_road = INF
    temp_idx = 0
    Q = deque([])
    for i in range(N):
        if board[idx][i] < min_road and not vi[i]:
            min_road = board[idx][i]
            temp_idx = i
            

for tc in range(int(input())):
    INF = 9999999999
    N, M, X = map(int, input().split())
    board = [[INF] * N for _ in range(N)]
    for i in range(M):
        x, y, c = map(int, input().split())
        board[x - 1][y - 1] = c
    for i in board:
        print(i)
    vi = [0] * N
    dik(0)
