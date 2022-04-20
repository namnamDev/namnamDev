def choice(pIdx, pN):
    if pIdx == N:
        global sumList
        t = len(sumList) - pN
        while t <= 1:
            sumList.append(0)
            t += 1
        sumList[pN] += 1
        return
    choice(pIdx + 1, pN)
    vi[pIdx] = 1
    choice(pIdx + 1, pN + arr[pIdx])
    vi[pIdx] = 0


N = int(input())
arr = list(map(int, input().split()))
vi = [0] * N
sumList = [0] * N
choice(0, 0)
print(sumList.index(0))