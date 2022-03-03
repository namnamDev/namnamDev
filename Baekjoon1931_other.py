import sys

sys.stdin = open("Baekjoon1931.txt")

n = int(input())
a = list(tuple(map(int, input().split())) for _ in range(n))
print(a)
a.sort(key=lambda x: x[0])
a.sort(key=lambda x: x[1])
print(a)
cur = a[0]
cnt = 1
for s, e in a:
    if (s >= cur[1]):
        cur = (s, e)
        cnt += 1
print(cnt)
