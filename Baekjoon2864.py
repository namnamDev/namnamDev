import sys

sys.stdin = open('Baekjoon2864.txt')

a, b = input().split()
m = 0
x = 0
for i in range(len(a)):
    m += (6 if a[i] == "5" else int(a[i])) * (10 ** (len(a) - 1 - i))
    x += (5 if a[i] == "6" else int(a[i])) * (10 ** (len(a) - 1 - i))
for g in range(len(b)):
    m += (6 if b[g] == "5" else int(b[g])) * (10 ** (len(b) - 1 - g))
    x += (5 if b[g] == "6" else int(b[g])) * (10 ** (len(b) - 1 - g))

print(x, m)
