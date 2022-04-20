def choice(depth, pNum):
    if depth == T - 2:
        global an
        an = max(an, pNum)
        # print(pNum)
        return

    for i in range(1, T - 1):
        if not vi[i]:
            vi[i] = 1
            added = 1
            for f in range(i + 1, T):
                if not vi[f]:
                    added *= arr[f]
                    break
            for f in range(i - 1, -1, -1):
                if not vi[f]:
                    added *= arr[f]
                    break
            choice(depth + 1, pNum + added)
            vi[i] = 0


T = int(input())
arr = list(map(int, input().split()))
vi = [0] * T
an = 0
choice(0, 0)
print(an)