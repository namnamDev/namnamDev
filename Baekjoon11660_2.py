import sys

sys.stdin = open('Baekjoon11660.txt')
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# board = [[0] * (N + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#     dp[1][i] = dp[1][i - 1] + board[0][i - 1]
#     dp[i][1] = dp[i - 1][1] + board[i - 1][0]
for i in board:
    print(i)
print()
for i in range(1, N):
    board[0][i] += board[0][i - 1]
    board[i][0] += board[i - 1][0]
# for i in board:
#     print(i)
for i in range(1, N):
    # board[0][i] += board[0][i - 1]
    # board[i][0] += board[i - 1][0]
    for g in range(1, N):
        board[i][g] += board[i - 1][g] + board[i][g - 1] - board[i - 1][g - 1]
for i in board:
    print(i)
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[y2 - 1][x2 - 1] - board[y2 - 1][x1 - 2] - board[y1 - 2][x2 - 1] + board[x1 - 2][y1 - 2])
# for i in range(1, N):
#     board[0][i] += board[0][i - 1]
#     board[i][0] += board[i - 1][0]
#
# dp[0] = [0] * (N + 1)
# for i in range(1, N):
#     for g in range(1, N):
#         board[i][g] += board[i - 1][g] + board[i][g - 1] - board[i - 1][g - 1]
#     dp[i] += board[i - 1]
# dp[N] += board[N - 1]
# # for i in range(1, N + 1):
# #     dp[i] += board[i - 1]
#
# board[x1 - 1][y1 - 1]
# for i in board:
#     print(i)
