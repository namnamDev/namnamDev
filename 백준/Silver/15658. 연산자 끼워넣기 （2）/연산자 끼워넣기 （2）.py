def op():
    res = arr[0]
    for i in range(N - 1):
        if visit[i] == 1:
            res += arr[i + 1]
        elif visit[i] == 2:
            res -= arr[i + 1]
        elif visit[i] == 3:
            res *= arr[i + 1]
        elif visit[i] == 4:
            if res < 0:
                res *= -1
                res //= arr[i + 1]
                res *= -1
            else:
                res //= arr[i + 1]

    return res


def lec(pidx):
    if pidx == N - 1:
        resList.append(op())
        return
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            visit[pidx] = i + 1
            lec(pidx + 1)
            visit[pidx] = i - 1
            oper[i] += 1


N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
total = sum(oper)
visit = [0] * (N - 1)
resList = []
lec(0)
print(max(resList))
print(min(resList))
