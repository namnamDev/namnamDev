import sys

sys.stdin = open('ExpertAcademy11765.txt')

for tc in range(int(input())):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]
    time_table.sort()
    dp = [0] * N
    dp[0] = 1

    for f in range(1, N):
        idx = f
        while idx > 0:
            idx -= 1
            if time_table[idx][1] <= time_table[f][0]:
                dp[f] += dp[idx] + 1
                break
            if idx == 0:
                dp[f] = 1

    print("#{} {}".format(tc + 1, max(dp)))
