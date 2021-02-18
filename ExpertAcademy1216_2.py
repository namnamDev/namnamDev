import sys

sys.stdin = open("ExpertAcademy1216.txt")
N = 100
for tc in range(1, 11):
    T = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(input())
    maxCnt = 0

    print("#{} {}".format(T, maxCnt))
