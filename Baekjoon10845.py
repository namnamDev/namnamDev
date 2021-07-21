import sys

sys.stdin = open('Baekjoon10845.txt')
from collections import deque

N = int(input())
Q = deque([])
an = ""
for _ in range(N):
    t = sys.stdin.readline().split()
    if t[0] == 'push':
        Q.append(t[1])
    elif t[0] == 'pop':
        if Q:
            an += str(Q.popleft()) + '\n'
            # print(Q.popleft())
        else:
            an += '-1\n'
    elif t[0] == 'size':
        an += str(len(Q)) + '\n'
        # print(len(Q))
    elif t[0] == 'empty':
        if Q:
            # print(0)
            an += '0\n'
        else:
            an += '1\n'
    elif t[0] == 'front':
        if Q:
            an += str(Q[0]) + "\n"
            # print(Q[0])
        else:
            an += '-1\n'
    elif t[0] == "back":
        if Q:
            an += str(Q[-1]) + "\n"
            # print(Q[-1])
        else:
            # print(-1)
            an += '-1\n'
print(an)
