import sys

sys.stdin = open('Baekjoon5430.txt')

from collections import deque

T = int(input())
for tc in range(T):
    cmd = list(input())
    N = int(input())
    arr = []
    answer = ""
    for i in input():
        if i.isdigit():
            arr.append(int(i))
    print(arr)
    Q = deque(arr)
    for cc in cmd:
        if cc == "R":
            Q.reverse()
            print(Q)
        else:
            if len(Q):
                Q.popleft()
                print(Q)
            else:
                answer = "error"
                break
    if answer != "error":
        answer = "["
        for ii in range(len(Q) - 1):
            answer += str(Q[ii]) + ","
        answer += str(Q[len(Q) - 1]) + "]"
        # for ii in arr:
        # answer += i
    print(answer)
