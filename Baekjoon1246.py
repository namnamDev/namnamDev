NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
li = []
for i in range(M):
    li+=[int(input())]
li.sort()

ansli = []
for i in range(M) :
    temp = M-i
    p = N
    if N > temp :
        p = temp
    sums = li[i]*p
    ansli += [(li[i],sums)]
maxs = 0
ans = ()
for g in ansli :
    if maxs < g[1] :
        maxs =g[1]
        ans = g
print(*ans)