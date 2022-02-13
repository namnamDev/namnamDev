import sys

sys.stdin = open("Baekjoon10988.txt")

a = list(input())
an = 1
for i in range(len(a)):
    if a[i] != a[len(a) - 1 - i]:
        an = 0
        break
print(an)
