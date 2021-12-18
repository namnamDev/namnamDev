import sys

sys.stdin = open('Baekjoon15829.txt')
N = int(input())
strs = input()
an = 0
for i in range(N):
    a = ord(strs[i]) - 96
    an += a * (31 ** i)
print(an)
