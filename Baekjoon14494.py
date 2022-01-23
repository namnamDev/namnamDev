import sys

sys.stdin = open("Baekjoon14494.txt")
n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
for i in range(n):
    board[i][0] = 1
board[0] = [1] * m
for i in range(1, n):
    for g in range(1, m):
        board[i][g] = board[i - 1][g] + board[i][g - 1] + board[i - 1][g - 1]
print(board[n - 1][m - 1] % (10 ** 9 + 7))
