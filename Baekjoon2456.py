N = int(input())
z = [[0] * 4 for _ in range(3)]
z2 = [0] * 3
for i in range(N):
    a, b, c = map(int, input().split())
    z[0][a] += 1
    z[1][b] += 1
    z[2][c] += 1
    z2[0] += a
    z2[1] += b
    z2[2] += c
aa = []
for i in range(3):
    if z2[i] == max(z2):
        aa.append(i)
an1 = 0
an2 = max(z2)
if len(aa) > 1:
    for i in aa:
        cnt = []
        maxCnt = 0
        for c in range(3, -1, -1):
            cnt.append(z[i][c])
            maxCnt = max(maxCnt, z[i][c])
        if cnt.count(maxCnt) == 1:
            an1 = cnt.index(maxCnt)
    print(an1, an2)
else:
    print(aa[0], z2[aa[0]])
