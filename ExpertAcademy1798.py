import sys
from collections import deque

sys.stdin = open('ExpertAcademy1798.txt')


def powerset(idx, day, val):
    if day > M:
        return
    time = 0
    while time<=9*60:

    powerset()


for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    print(N, M)
    for i in range(N - 1):
        line = list(map(int, input().split()))
        idx = 0
        for g in range(i + 1, N):
            board[i][g] = line[idx]
            board[g][i] = line[idx]
            idx += 1
    point = [0] * N
    start = 0
    for i in range(N):
        point[i] = list(input().split())
        if point[i] == ['A']:
            start = i

    for i in board:
        print(i)

    for g in point:
        print(g)
