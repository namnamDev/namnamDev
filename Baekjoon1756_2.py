import sys

sys.stdin = open("Baekjoon1756.txt")

D, N = map(int, input().split())
arr, end = list(map(int, input().split())) + [0], list(map(int, input().split()))
visited = [0] * (D + 1)
dp = [0] * (D + 1)
temp = arr[0]
maxs = [0, 0]
dp2 = []
for i in range(D + 1):
    if arr[i] < temp:
        dp2.append([temp, i])
        temp = arr[i]
    dp[i] = temp
print(dp)
dp2.append([0, D])
print(dp2)
maxss = [0, 0]
for i in range(N):
    for g in range(len(dp2)):
        if maxss == dp2[g]:
            dp2[g][1] -= 1
            maxss = dp2[g]
            break
        elif end[i] > dp2[g][0]:
            dp2[g - 1][1] -= 1
            maxss = dp2[g - 1]
            print(end[i], dp2[g], dp2)
            break
print(maxss)
# for i in end:
#     if i < maxs[0] and arr[maxs[1] - 1] <= i:
#         maxs[1] -= 1
#         visited[maxs[1]] = 1
#     else:
#         for g in range(D):
#             if visited[g] == 0:
#                 if i > arr[g]:
#                     maxs = [i, g]
#                     visited[g] = 1
#                     break
#             else:
#                 visited[g - 1] = 1

# print(visited.index(1))
