import sys

sys.stdin = open('Baekjoon1197.txt')
V, E = map(int, input().split())
board = [[0] * V for _ in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    board[a - 1][b - 1] = c
    board[b - 1][a - 1] = c
for i in board:
    print(i)
