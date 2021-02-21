import sys

sys.stdin = open("ExpertAcademy1216.txt")
N = 100
for tc in range(1, 11):
    T = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(input())

    for g in range(N):
        for i in range(N):
            if arr[g][i] != arr[g][N-i-1]:
                break
            if arr[i][g] != arr[i][N-g-1]:
                break
            print(g, i)


    # print("#{} {}".format(T, maxCnt))
