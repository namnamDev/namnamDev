import sys

sys.stdin = open("ExpertAcademy1859.txt")


def half(li):
    global sums
    maxN = li[0]
    maxIdx = 0
    m = len(li)
    for g in range(m):
        if maxN < arr[g]:
            maxN = arr[g]
            maxIdx = g

    # print(maxIdx, li[maxIdx])
    if maxIdx != m - 1:
        half1 = li[:maxIdx + 1]
        half2 = li[maxIdx + 1::]
        # print(half1)
        # print(half2)
        half(half1)
        half(half2)
    else:
        sums += maxN * (m) - sum(li)
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxIdx = 0
    # dpli = [0] * N
    i = 0
    sums = 0
    half(arr)
    print("#{} {}".format(tc, sums))
