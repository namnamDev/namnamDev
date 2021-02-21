N, S = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
for i in range(1, 1 << N):
    sums = 0
    for g in range(i):
        if i & (1 << g):
            sums += li[g]
    if sums == S:
        cnt += 1
print(cnt)
