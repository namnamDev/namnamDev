import sys

sys.stdin = open('Baekjoon10866.txt')
from collections import deque

N = int(input())
Q = deque([])
an = ""
for _ in range(N):
    t = input().split()
    a = t[0]
    if a == "push_back":
        Q.append(t[1])
    elif a == "push_front":
        Q.appendleft(t[1])
    elif a == "front":
        if Q:
            an += str(Q[0]) + "\n"
        else:
            an += "-1\n"
    elif a == "back":
        if Q:
            an += str(Q[-1]) + "\n"
        else:
            an += "-1\n"
    elif a == "size":
        an += str(len(Q)) + "\n"
    elif a == "empty":
        if len(Q):
            an += "0\n"
        else:
            an += "1\n"
    elif a == "pop_back":
        if Q:
            an += str(Q.pop()) + "\n"
        else:
            an += "-1\n"
    elif a == "pop_front":
        if Q:
            an += str(Q.popleft()) + "\n"
        else:
            an += "-1\n"
print(an)
