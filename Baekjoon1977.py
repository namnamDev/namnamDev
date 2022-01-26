import sys

sys.stdin = open("Baekjoon1977.txt")
M, N = int(input()), int(input())
m = 1
while m < M:
    if m ** 2 > M:
        break
    m += 1
arr = []
while m ** 2 <= N:
    arr.append(m ** 2)
    m += 1
if len(arr):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
