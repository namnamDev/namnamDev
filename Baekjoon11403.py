import sys

sys.stdin = open("Baekjoon11403.txt")
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
anVi = [[0] * N for _ in range(N)]
bigVi = [0] * N
for i in range(N):
    if not bigVi[i]:
        bigVi[i] = 1
        nList = [i]
        vi = [0] * N
        Q = deque([i])
        vi[i] = 1
        while Q:
            now = Q.popleft()
            tb = board[now]
            print(tb)
            for j in range(N):
                if not vi[j] and tb[j]:
                    vi[j] = 1
                    Q.append(j)
                    nList.append(j)
        print(i, nList)
        for ii in nList:
            anVi[ii] = vi

for i in anVi:
    print(*i)
#
