import sys

sys.stdin = open("ExpertAcademy1860mini.txt")
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(N, M, K, tc, arr)
    dpli = [0] * N
    i = 0
    s = 0
    bread = 0
    an = "Impossible"
    while s <= 11111 and i < N:
        # print(i, s, bread)
        s += 1
        if s % M == 0:
            bread += K
            print("-", K, bread)

        while arr[i] <= s:
            print(i, arr[i], s, bread)
            i += 1
            print(arr)
            if i == N - 1 and bread <= 0:
                break
            arr[i] = 0
            bread -= 1
    if arr[N - 1] == 0:
        an = "Possible"
    # print(arr)
    print("#{} {}".format(tc, an))
