import sys

sys.stdin = open("Baekjoon11053.txt")
n, arr = int(input()), list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    tm = 0
    for ii in range(i - 1, -1, -1):
        if arr[i] > arr[ii]:
            tm = max(tm, dp[ii])
    dp[i] = tm + 1
print(max(dp))
