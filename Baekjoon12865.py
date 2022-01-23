import sys

sys.stdin = open("Baekjoon12865.txt")
n, k = map(int, input().split())
aa = [list(map(int, input().split())) for _ in range(n)]
aa.sort()
print(aa)
values = [0] * n
weights = [0] * n
values[0] = aa[0][1]
weights[0] = aa[0][0]
for i in range(1, n):
    nowW = aa[i][0]
    nowV = aa[i][1]
    for f in range(i - 1, -1, -1):
        tempW = weights[f] + nowW
        if tempW <= k:
            weights[i] = tempW
            values[i] = nowV + values[f]
            break
        # else:
        #     values[i] = values[f]
        #     weights[i] =
print(values)
print(weights)
