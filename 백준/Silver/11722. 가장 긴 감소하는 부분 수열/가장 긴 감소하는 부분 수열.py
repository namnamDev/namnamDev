T = int(input())
N = list(map(int, input().split()))
dp = [1] * T
for t in range(T - 2, -1, -1):
    for i in range(t + 1, T):
        if N[t] > N[i]:
            dp[t] = max(dp[t], dp[i] + 1)
print(max(dp))