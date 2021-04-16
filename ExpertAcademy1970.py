import sys
import time

sys.stdin = open("ExpertAcademy1970.txt")
for tc in range(int(input())):
    N = int(input())
    arr = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        temp = N // money[i]
        if temp:
            N -= temp * money[i]
            arr[i] = temp
    print('#{}'.format(tc + 1))
    print(*arr)
