while True:
    try:
        s, t = input().split()
    except:
        break
    lenS = len(s)
    lenT = len(t)
    n = 0
    m = 0
    cnt = 0
    an = "No"
    while n < lenS:
        # print(n, m, s[n], t[m])
        if s[n] == t[m]:
            n += 1
            cnt += 1
        m += 1
        if m == lenT:
            break
    if cnt == lenS:
        an = "Yes"
    print(an)
