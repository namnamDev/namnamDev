#00
#10 11
#20 21 22
#30 31 32 33

t = int(input())
for f in range(t):
    n = int(input())
    b = []
    for i in range(n+1):
        li = []
        for g in range(i):
            t =0
            if g == 0 or g == i-1 :
                t = 1
            else : 
                t = b[i-1][g-1] +b[i-1][g]
            li+=[t]
        b+=[li]
    b.pop(0)
    print(f'#{f+1}')
    for f in b:
        print(*f)