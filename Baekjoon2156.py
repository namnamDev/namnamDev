import sys

sys.stdin = open("Baekjoon2156.txt")
n = int(input())
board = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = board[0]
dp[1] = dp[0] + board[1]
print(board)
print(dp)
