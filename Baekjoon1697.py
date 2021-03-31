def powerset(n, m, cnt):
    global mins
    if cnt > mins:
        return
    if n == m:
        mins = cnt
        return
    else:
        diry = [abs(m - (n - 1)), abs(m - (n + 1)), abs(m - 2 * n)]
        print(n, m, diry)
        diry.sort()
        for i in diry:
            powerset(m - i, m, cnt + 1)


N, M = map(int, input().split())
mins = abs(M - N)
powerset(N, M, 0)
print(mins)
