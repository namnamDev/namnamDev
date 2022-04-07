N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]
for y in range(1, N):
    dp[y][0] += dp[y - 1][0] + board[y][0]
for x in range(1, M):
    dp[0][x] += dp[0][x - 1] + board[0][x]

for y in range(1, N):
    for x in range(1, M):
        dp[y][x] = max(dp[y - 1][x], dp[y][x - 1]) + board[y][x]
print(dp[-1][-1])