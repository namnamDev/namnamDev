import sys

sys.stdin = open("Baekjoon1620.txt")

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]
for a in arr2:
    if a.isdigit():
        print(arr[int(a) - 1])
    else:
        print(arr.index(a) + 1)
