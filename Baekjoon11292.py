while True:
    T = int(input())
    if not T :
        break
    c,h= {},[]
    for i in range(T):
        a = input().split()
        a_1 = int(float(a[1])*100)
        if not c.get(a_1) :
            c[a_1] = [a[0]]
            h+=[a_1]
        else :
            c[a_1].append(a[0])
    maxhi = max(h)
    # print(maxhi)
    print(*c[maxhi])