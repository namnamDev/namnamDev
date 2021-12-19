import sys

sys.stdin = open('Baekjoon1240.txt')
N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
for i in range(N - 1):
    y, x, m = map(int, input().split())
    y -= 1
    x -= 1
    board[y][x] = m
    board[x][y] = m
