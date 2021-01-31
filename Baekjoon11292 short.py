while True:
    T = int(input())
    if not T :
        break
    c,h= {},[]
    for i in range(T):
        a = input().split()
        b = float(a[1])
        if not c.get(b) :
            c[b] = [a[0]]
            h+=[b]
        else :
            c[b]+=[a[0]]
    m = max(h)
    print(*c[m])