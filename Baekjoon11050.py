import sys

sys.stdin = open("Baekjoon11050.txt")
N, M = map(int, input().split())
arr = [1, 1]
for i in range(2, N + 1):
    arr.append(arr[i - 1] * i)
print(arr[N] // (arr[M] * arr[N - M]))
