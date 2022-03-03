import sys
from collections import deque

sys.stdin = open("Baekjoon1932.txt")
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = []
for i in range(1, N + 1):
    dp.append([0] * i)
dp[0][0] = board[0][0]
for i in range(1, N):
    dp[i][0] = board[i][0] + dp[i - 1][0]
    dp[i][-1] = board[i][-1] + dp[i - 1][-1]
for y in range(1, N):
    tArr = dp[y - 1]
    for x in range(1, len(tArr)):
        wll = dp[y - 1][x - 1]
        wrr = dp[y - 1][x]
        dp[y][x] = max(wll, wrr) + board[y][x]
print(max(dp[-1]))
#    0
#   0 1
#  0 1 2
# 0 1 2 3
