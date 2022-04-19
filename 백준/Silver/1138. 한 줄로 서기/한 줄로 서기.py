def check():
    tarr = [0] * N
    for i in range(N):
        now = parr[i] - 1
        for ii in range(i):
            if now < parr[ii]:
                tarr[now] += 1
    for i in range(N):
        if tarr[i] != arr[i]:
            return False
    global an
    an = " ".join(list(map(str, parr)))
    return True


def choice(idx):
    if an != "":
        return
    if idx == N:
        check()
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            parr[idx] = i + 1
            choice(idx + 1)
            visit[i] = 0


N = int(input())
arr = list(map(int, input().split()))
visit = [0] * N
parr = [0] * N
an = ""
choice(0)
print(an)