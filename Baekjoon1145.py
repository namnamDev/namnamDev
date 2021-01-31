li = list(map(int,input().split()))
baslist = []
for i in li:
    bas = []
    temp = i
    lev = 1
    while temp != 1:
        if not temp%lev:
            bas+=[lev]
            temp = temp//lev
        print(temp)
        lev+=1
    baslist.append(bas)
print(baslist)