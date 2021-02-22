# 00
# 10 11
# 20 21 22
# 30 31 32 33


t = int(input())
b = []
for f in range(t):
    n = int(input())
    lenb = len(b)
    if lenb < n + 1:
        for i in range(lenb, n + 1):
            li = []
            for g in range(i):
                t = 0
                if g == 0 or g == i - 1:
                    t = 1
                else:
                    t = b[i - 1][g - 1] + b[i - 1][g]
                li += [t]
            b += [li]
    print('#{}'.format(f + 1))
    for g in range(1, n + 1):
        print(*b[g])
