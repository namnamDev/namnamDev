import sys

sys.stdin = open("Baekjoon1915.txt")
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
maxs = 0
for i in range(N):
    for g in range(M):
        if arr[i][g]:
            if arr[i - 1][g] and arr[i][g - 1] and arr[i - 1][g - 1]:
                temp = [dp[i - 1][g], dp[i][g - 1], dp[i - 1][g - 1]]
                dp[i][g] = min(temp) + 1
                if maxs < dp[i][g]:
                    maxs = dp[i][g]

            else:
                dp[i][g] = 1
        else:
            dp[i][g] = 0
for i in arr:
    print(i)
print()

for i in dp:
    print(i)

print(maxs ** 2)
