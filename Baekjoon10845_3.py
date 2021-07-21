import sys

sys.stdin = open('Baekjoon10845.txt')
from collections import deque

N = int(input())
Q = deque([])
for _ in range(N):
    t = input().split()
    if t[0] == 'push':
        Q.append(t[1])
    elif t[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif t[0] == 'size':
        print(len(Q))
    elif t[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif t[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif t[0] == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)
