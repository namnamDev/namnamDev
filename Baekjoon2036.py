import sys
from collections import deque

sys.stdin = open("Baekjoon2036.txt")
n = int(input())
Q1 = []
Q2 = []
for i in range(n):
    num = int(input())
    if num <= 0:
        Q1.append(num)
    else:
        Q2.append(num)
Q1.sort()
Q2.sort(reverse=True)
print(Q1, Q2)
cnt = 0
for i in range(len(Q1)//2):
