import sys
T = int(input())
Tlist = [None] * T

for i in range(T):
    score = [0] *101
    miniT = int(input())
    line = input().split()
    maxs = 0
    for g in line:
        score[int(g)] += 1
    print('-----------')
    print(score)

    for f in score:
        if f >= maxs:
            maxs = f
    Tlist[i] = score.index[maxs]
    

for i in range(T) :
    print(f'#{i+1} {Tlist[i]}')
