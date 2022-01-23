import sys

sys.stdin = open("Baekjoon1495.txt")
N, S, M = map(int, input().split())
arr = list(map(int, input().split()))
vi = [0] * (N+1)
vi[0] = S

print(N, S, M)
an = 0
for i in range(1,N):
    if vi[i-1] + arr[i] <= M or vi[i-1] + arr[i]
