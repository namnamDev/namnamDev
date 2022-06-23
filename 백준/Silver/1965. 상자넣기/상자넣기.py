N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for fir in range(N):
    for sec in range(fir, -1, -1):
        if arr[fir] > arr[sec]:
            dp[fir] = max(dp[fir], dp[sec] + 1)
print(max(dp))