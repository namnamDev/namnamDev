N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = arr[i]
    for f in range(i - 1, -1, -1):
        if arr[i] > arr[f]:
            dp[i] = max(dp[i], dp[f] + arr[i])
print(max(dp))