import sys

sys.stdin = open("Baekjoon1931.txt")

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1] * N
for n in range(1, N):
    now = arr[n]
    for l in range(n - 1, -1, -1):
        lefts = arr[l]
        dp[n] = dp[l]
        if lefts[1] <= now[0]:
            dp[n] += 1
            break
print(arr)
print(dp[-1])
