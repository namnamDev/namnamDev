import sys

sys.stdin = open("Baekjoon2156.txt")
n = int(input())
board = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = board[0]
dp[1] = dp[0] + board[1]
dp[2] = board[0]
for i in range(2, n):
    if board[i - 1] > board[i - 2]:
        dp[i] = board[i - 1] + dp[i - 1]
    else:
        dp[i] = board[i - 2] + dp[i - 2]
    # dp[i] = max(board[i - 1], board[i - 2]) + board[i]
print(dp)
