import sys

sys.stdin = open('Baekjoon11660.txt')
# input = sys.stdin.readline().split()
N, M = map(int, sys.stdin.readline().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]
board = [list(map(int, sys.stdin.readline().split()))]
for i in range(1, N + 1):
    dp[1][i] = board[0][i - 1] + dp[1][i - 1]
for i in range(2, N + 1):
    board.append(list(map(int, sys.stdin.readline().split())))
    for ii in range(1, N + 1):
        dp[i][ii] = board[i - 1][ii - 1] + dp[i - 1][ii] + dp[i][ii - 1] - dp[i - 1][ii - 1]
for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1])
    # a = dp[y2][x1:x2 + 1]
    # b = dp[y1 - 1][x1:x2 + 1]
    # print(sum(a) - sum(b))
