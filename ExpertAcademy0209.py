import sys
sys.stdin = open("ExpertAcademy0209.txt")
T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = []
    for g in range(N):
        arr += [(list(map(int, input())))]
    # print(arr)
    center = N//2
    sums = 0
    temp = []
    for f in range(center):
        temp = arr[f][center-f:center+f+1]

        for ff in temp:
            sums += ff

    for j in range(center, N):
        temp = arr[j][j-center:N-j+2]
        print(temp, len(temp))
        for ff in temp:
            sums += ff
    print("#{} {}".format(i, sums))
        # print(j,j-center,N-j+2)
        # print(temp)
    # print("--")
    # print(arr)