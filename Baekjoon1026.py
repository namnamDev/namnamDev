import sys

sys.stdin = open("Baekjoon1026.txt")
a = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
aa = 0
for i in range(a):
    aa += A[i] * B[i]
print(aa)
