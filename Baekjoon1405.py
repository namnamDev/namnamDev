import sys

sys.stdin = open('Baekjoon1405.txt')


def back(paArr, move, now):
    if len(move) == N:
        return
    for i in range(1, 5):
        dirs[arr[i]]


arr = list(map(int, input().split()))
print(arr)
N = arr[0]
now = [0, 0]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
