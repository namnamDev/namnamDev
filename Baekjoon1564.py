import sys

sys.stdin = open("Baekjoon1564.txt")
N = int(input())
print(N)
a = 1
for i in range(1, N + 1):
    a *= i
    if not a % 10:
        a //= 10
print(a)
