import sys

sys.stdin = open("Baekjoon1003.txt")

dp = [[0] * 2 for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]


def fibo(n):
    if n <= 1:
        return dp[n]

    if not dp[n][0] and not dp[n][1]:
        a1 = fibo(n - 1)
        a2 = fibo(n - 2)
        dp[n] = [a1[0] + a2[0], a1[1] + a2[1]]
    return dp[n]


for tc in range(int(input())):
    n = int(input())
    fibo(n)
    print(*dp[n])
# for ii in range(2, 41):
#     a = False
#     b = False
#     if dp0[ii] == dp0[ii - 1] + dp0[ii - 2]:
#         a = True
#     if dp1[ii] == dp1[ii - 1] + dp1[ii - 2]:
#         b = True
#     print(a, b)
