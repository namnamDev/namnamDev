import sys

sys.stdin = open('Baekjoon11660.txt')
N, M = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]
board = [list(map(int, input().split()))]
dp[1] = [0] + board[0]
for i in range(2, N + 1):
    board.append(list(map(int, input().split())))
    for ii in range(1, N + 1):
        dp[i][ii] = board[i - 1][ii - 1] + dp[i - 1][ii]
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    a = dp[y2][x1:x2 + 1]
    b = dp[y1 - 1][x1:x2 + 1]
    print(sum(a) - sum(b))
