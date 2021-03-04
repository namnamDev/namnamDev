import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1225.txt")
for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    N = len(arr)
    g = 1
    while True:
        # print(g, end="")
        arr.append(arr.pop(0) - g)
        g = g % 5 + 1
        # print(arr)
        if arr[N - 1] <= 0:
            arr[N - 1] = 0
            break
    print("#{}".format(tc), end=" ")
    print(*arr)
# 1 6 2 2 9 4 1 3 0
# 2 9 7 9 5 4 3 8 0
# 3 8 7 1 6 4 3 5 0
# 4 7 5 8 4 8 1 3 0
# 5 3 8 7 4 4 7 4 0
# 6 6 7 5 9 6 8 5 0
# 7 7 6 8 3 2 5 6 0
# 8 9 2 1 7 3 6 3 0
# 9 4 7 8 1 2 8 4 0
# 10 6 8 9 5 8 5 2 0
