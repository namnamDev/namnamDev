import sys

sys.stdin = open('Baekjoon2475.txt')
a = list(map(int, input().split()))
an = 0
for i in a:
    an += i ** 2
print(an % 10)
