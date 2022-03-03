import sys
from pathlib import Path

sys.stdin = open(Path(__file__).stem + ".txt")
from collections import deque

N = int(input())
arr = list(map(int, input().split()))
# c = []
# for i in range(N):
#     c.append([arr[i], i + 1])
# an = [1]
# now = c.pop(0)
# m = now[0] % len(c)
# idx = m - 1
# while len(c) > 1:
#     now = c.pop(idx)
#     an.append(now[1])
#     idx = (idx + now[0]) % len(c)
# an.append(c[0][1])
# print(*an)

# vi 놓고 남은 별풍갯수 세가면서 풀기
