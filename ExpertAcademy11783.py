import sys
from collections import deque

sys.stdin = open('ExpertAcademy11783.txt')


def die(idx, val):
    temp = board[idx]
    temp_idx = 0
    temp_min = 9999999999
    if vi[N]:
        return
    for i in range(N):
        if 0 < temp[i] < temp_min and not vi[i]:
            print(i, temp_min)
            temp_min = temp[i]
            temp_idx = i
    if temp_min < val:
        print(temp_min, val, 'q12')
        vi[temp_idx] = val + temp_min
        die(temp_idx, val + temp_min)


for tc in range(int(input())):
    N, E = map(int, input().split())
    board = [[0] * (N + 1) for _ in range(N + 1)]
    vi = [0] * (N + 1)
    for i in range(E):
        start, end, length = map(int, input().split())
        board[start][end] = length
    for i in board:
        print(i)
    die(0, 0)
    print(vi)
