import sys

sys.stdin = open('Baekjoon5585.txt')
a = 1000 - int(input())
cnt = 0
arr = [1000, 500, 100, 50, 10, 5, 1]
for i in arr:
    t = a // i
    if t:
        cnt += t
        a -= t * i
print(cnt)
