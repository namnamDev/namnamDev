import sys

sys.stdin = open('Baekjoon1195.txt')

N, M = map(int, input().split())
board = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    board[B].append(A)

an = {}
maxs = 0
for idx in range(1, N + 1):
    vi = [0] * (N + 1)
    vi[idx] = 1
    cnt = 0
    Q = [idx]
    while Q:
        now = Q.pop()
        tempArr = board[now]
        for tempIdx in range(len(tempArr)):
            if not vi[tempArr[tempIdx]]:
                vi[tempArr[tempIdx]] = 1
                Q.append(tempArr[tempIdx])
                cnt += 1
    if not an.get(cnt):
        an[cnt] = [idx]
    else:
        an[cnt].append(idx)
    maxs = max(cnt, maxs)

print(*an.get(maxs))
