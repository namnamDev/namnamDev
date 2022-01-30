import sys

sys.stdin = open("Baekjoon9461.txt")
dp = [1, 1, 1]
for _ in range(int(input())):
    a = int(input())
    while len(dp) < a:
        dp.append(dp[-2] + dp[-3])
    print(dp[a - 1])
