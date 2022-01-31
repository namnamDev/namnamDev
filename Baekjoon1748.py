import sys

sys.stdin = open('Baekjoon1748.txt')
x = int(input())
a = 100000000
n = 1
# 1~9 ----1
# 10~99 --2
# 100~999-3
an = 9
print(list(range(10, 100)))
print(len(list(range(10, 100))))
while 10 ** (n - 1) < x:
    print(n)
    an += n * 9 * (10 ** (n - 1))
    n += 1
print(an)
