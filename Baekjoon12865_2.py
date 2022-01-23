import sys

sys.stdin = open("Baekjoon12865.txt")
n, k = map(int, input().split())
aa = [list(map(int, input().split())) for _ in range(n)]
aa.sort()
values = [0] * n
weights = [0] * n
values[0] = aa[0][1]
weights[0] = aa[0][0]
for i in range(1, n):
    nowW = aa[i][0]
    nowV = aa[i][1]
    weights[i] = nowW
    values[i] = nowV
    print(i, "++")
    for f in range(i - 1, -1, -1):
        tempW = weights[f] + nowW
        tempV = values[f] + nowV
        print(f, tempW)
        if tempW <= k:
            if values[i] <= tempV:
                weights[i] = tempW
                values[i] = nowV + values[f]
print(aa)
print(values)
print(weights)
