while True:
    try:
        s, t = input().split()
    except:
        break
    d = len(s)
    e = len(t)
    n, m = 0, 0
    an = "No"
    while m < e:
        # print(n, m, s[n], t[m], d, e)
        if s[n] == t[m]:
            n += 1
        if n == d:
            an = "Yes"
            break
        m += 1
    print(an)
