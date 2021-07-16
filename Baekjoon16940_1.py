import sys

sys.stdin = open('Baekjoon16940.txt')
from collections import deque

N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
vi = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1
order = list(map(int, input().split()))
Q = deque([order[0]])
vi[order[0]] = 1
order[order.index(vi[order[0]])] = -1
maxIdx = 0
answer = 1
while Q:
    now = Q.popleft()
    for i in range(1, N + 1):
        if not vi[i] and board[now][i]:
            vi[i] = vi[now] + 1
            temp = order.index(i)
            order[temp] = -1
            if maxIdx < temp:
                maxIdx = temp
            else:
                answer = 0
                # print(order, maxIdx)
            # print(order.index(i), order.index(now))
            # if order.index(i) < order.index(now):
            #     answer = 0
            #     Q = []
            #     break
            # if maxIdx < i:
            #     print(maxIdx, vi[maxIdx], i, vi[i])
            #     maxIdx = i
            # else:
            #     if vi[maxIdx] < vi[i]:
            #         print(maxIdx, vi[maxIdx], i, vi[i])
            #         answer = 0
            #         Q = []
            #         break

            Q.append(i)
print(answer)
