import sys

sys.stdin = open("Baekjoon2491.txt")

N = int(input())
arr = list(map(int,input().split()))
dp1 = [1] * N
dp2 = [1] * N
# dp1[0], dp2[0] = 1, 1
for i in range(1, N):
    f = i - 1
    # for f in range(i-1, -1, -1):
    if arr[i] >= arr[f]:
        dp1[i] = dp1[f] + 1
        # break

for i in range(1, N):
    f = i - 1
    # for f in range(i-1, -1, -1):
    if arr[i] <= arr[f]:
        dp2[i] = dp2[f] + 1
        # break
print(max(max(dp1), max(dp2)))
