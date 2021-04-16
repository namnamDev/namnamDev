import sys

sys.stdin = open('ExpertAcademy11760.txt')

for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    temp = list(range(N))
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = board[0][0]
    print(1)
    # [6, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0]
    for i in range(1, N):
        dp[0][i] += board[0][i] + dp[0][i - 1]
        dp[i][0] += board[i][0] + dp[i - 1][0]
    print(2)
    # [6, 13, 14, 24, 26]
    # [16, 0, 0, 0, 0]
    # [25, 0, 0, 0, 0]
    # [26, 0, 0, 0, 0]
    # [34, 0, 0, 0, 0]
    for i in dp:
        print(i)

    for i in range(1, N):
        for g in range(1, N):
            dp[i][g] = min(dp[i - 1][g], dp[i][g - 1]) + board[i][g]
    print(3)
    # [6, 13, 14, 24, 26]
    # [16, 15, 21, 26, 35]
    # [25, 18, 20, 29, 35]
    # [26, 24, 28, 30, 39]
    # [34, 27, 35, 32, 33]
    for i in dp:
        print(i)
    print("#{} {}".format(tc + 1, dp[N - 1][N - 1]))
