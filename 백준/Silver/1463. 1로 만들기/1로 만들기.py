T = int(input())
dp = [0] * (T + 5)
dp[2] = 1
dp[3] = 1
for i in range(4, T + 1):
    arr = []
    if not i % 2:
        arr.append(dp[i // 2])
    if not i % 3:
        arr.append(dp[i // 3])
    arr.append(dp[i - 1])
    dp[i] = min(arr) + 1
print(dp[T])