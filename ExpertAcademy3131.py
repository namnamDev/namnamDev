for g in range(2, 10 ** 6):
    t = 2
    while True:
        # print(g, t)
        if g % t == 0 and g != t:
            break
        if t == g:
            print(g, end=" ")
            break
        t += 1
