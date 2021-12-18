import sys

sys.stdin = open('Baekjoon1927.txt')
from collections import deque

T = int(input())
Q = deque([])
for i in range(T):
    a = int(input())
    if a == 0:
        if Q:
            mins = min(Q)
            Q.remove(mins)
            print(mins)
        else:
            print(0)
    else:
        Q.append(a)
