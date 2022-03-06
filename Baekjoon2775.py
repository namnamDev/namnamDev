import sys

sys.stdin = open("Baekjoon2775.txt")

dp = [[1]]
for tc in range(int(input())):
    k = int(input())
    n = int(input())
    for i in range(len(dp[0]), n):
        dp[0].append(dp[0][-1] + 1)
    for y in range(1, len(dp)):
        for x in range(len(dp[y]), n):
            dp[y].append(dp[y][-1] + dp[y - 1][x])
    for y in range(len(dp), k + 1):
        tArr = [dp[-1][0]]
        for x in range(1, n):
            tArr.append(dp[-1][x] + tArr[-1])
        dp.append(tArr)
    # for i in dp:
    #     print(i)
    print(dp[k][n - 1])
    # 1 2 3 4 5
    # 1 3 6 10 15
    # 1 4 10 20 35
