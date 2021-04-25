import sys
from collections import deque

sys.stdin = open('ExpertAcademy7465.txt')


def my_find(num):
    if arr[num] == num:
        return num
    return my_find(arr[num])


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(range(N))
    temp = []
    for i in range(M):
        fir, sec = map(int, input().split())
        arr[my_find(sec - 1)] = my_find(fir - 1)
    an = 0
    for i in range(N):
        if i == arr[i]:
            an += 1

    print('#{} {}'.format(tc + 1, an))
