import sys

sys.stdin = open("Baekjoon11066.txt")
for tc in range(int(input())):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * K
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for fir in range(2, K):
        # t = arr[fir - 1]
        # for sec in range(fir - 2, -1, -1):
        #     t = min(t, arr[sec])
        dp[fir] = dp[fir - 1] + arr[fir]
        # 40 30 30
    # 70 30 100
    print(arr)
    print(dp)
