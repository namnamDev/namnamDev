import sys

sys.stdin = open("Baekjoon5554.txt")
a = sum([int(input()) for _ in range(4)])
print(a // 60)
print(a % 60)
