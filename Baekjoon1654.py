import sys

sys.stdin = open("Baekjoon1654.txt")
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
arr.sort()
t = arr[-1]
an = 0
for idx in range(t, 0, -1):
    aa = 0
    for i in range(K):
        aa += arr[i] // idx
        if aa > N:
            aa = -1
            break
    if aa == N:
        an = idx
        break
print(an)
