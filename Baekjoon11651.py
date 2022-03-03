import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")
N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])
arr.sort()
for i in arr:
    print(i[1], i[0])
