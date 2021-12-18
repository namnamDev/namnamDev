import sys

sys.stdin = open('Baekjoon1966.txt')
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    aa = list(map(int, input().split()))
    cnt = [0] * 10
    bb = []
    for i in range(N):
        cnt[aa[i]] += 1
        bb.append([aa[i], i])
    Q = deque(bb)
    an = 0
    printed = 0
    for g in range(9, 0, -1):
        while cnt[g]:
            if Q[0][0] == g:
                printed += 1
                cnt[g] -= 1
                temp = Q.popleft()
                if temp[1] == M:
                    an = printed
                    break
            else:
                Q.append(Q.popleft())
        if an:
            break

    print(an)
