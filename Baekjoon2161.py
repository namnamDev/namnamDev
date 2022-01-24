import sys

from collections import deque

sys.stdin = open("Baekjoon2161.txt")
N = int(input())
arr = list(range(1, N + 1))
an = [arr.pop(0)]
while arr:
    arr.append(arr.pop(0))
    an.append(arr.pop(0))
print(*an)
