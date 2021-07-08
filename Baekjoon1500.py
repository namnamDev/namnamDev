def choice(s, idx, arr):
    # print(s, idx, arr)
    if len(arr) == K - 1:
        s += S - sum(arr) - 1
        arr += [S - sum(arr)]
        if s == S:
            tempan = 1
            for i in arr:
                tempan *= i
            # print(arr, tempan)
            global an
            an = max(tempan, an)
        return
    for i in range(idx, S - sum(arr)):
        choice(s + i, i, arr + [i])
    return


S = 10
K = 3
# S, K = map(int, input().split())
an = 0
choice(1, 1, [])
print(an)
