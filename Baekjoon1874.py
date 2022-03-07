import sys

sys.stdin = open("Baekjoon1874.txt")
n = int(input())
arr = list(range(1, n + 1))
stack = []
for _ in range(n):
    t = int(input())
