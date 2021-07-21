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
        else:
            an += '-1\n'
    elif t[0] == 'size':
        an += str(len(Q)) + '\n'
    elif t[0] == 'empty':
        if Q:
            an += '0\n'
        else:
            an += '1\n'
    elif t[0] == 'front':
        if Q:
            an += str(Q[0]) + "\n"
        else:
            an += '-1\n'
    elif t[0] == "back":
        if Q:
            an += str(Q[-1]) + "\n"
        else:
            an += '-1\n'
print(an)
