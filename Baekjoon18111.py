import sys

sys.stdin = open("Baekjoon18111.txt")
N, M, B = map(int, input().split())
cnts = [0] * (257)
print(N, M, B)
maxs = 0
mins = 257
howto = [0, 0]
for i in range(N):
    line = list(map(int, input().split()))
    for g in line:
        cnts[g] += 1
        maxs = max(g, maxs)
        mins = min(g, mins)
print(mins, maxs)
print(cnts)
while mins < maxs:
    if cnts[mins] < cnts[maxs] * 2:
        if B:
            print(mins, maxs, cnts[mins], cnts[maxs])
            cnts[mins] -= 1
            cnts[maxs] += 1
            B -= 1
            howto[0] += 1
        else:
            cnts[mins] += 1
            cnts[maxs] -= 1
            howto[0] += 1
    else:
        cnts[maxs] -= 1
        howto[0] += 1
    if not cnts[mins]:
        mins += 1
    if not cnts[maxs]:
        maxs -= 1
    print(cnts)
print(howto)

print(cnts)
