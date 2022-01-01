import sys

sys.stdin = open('Baekjoon16928.txt')

from collections import deque

N, M = map(int, input().split())
board = [0] * 100
vi = [0] * 100
for i in range(N):
    x, y = map(int, input().split())
    board[x - 1] = y - 1
for i in range(M):
    u, v = map(int, input().split())
    board[u - 1] = v - 1
vi[0] = 1
Q = deque([0])
while Q:
    now = Q.popleft()
    for i in range(1, 7):
        wy = now + i
        if wy < 100 and not vi[wy]:
            vi[wy] = vi[now] + 1

            if board[wy] and not vi[board[wy]]:
                vi[board[wy]] = vi[now] + 1
                Q.append(board[wy])

            else:
                Q.append(wy)

    if vi[-1]:
        break
        # if wy < 100 and vi[wy] > vi[now] + 1:
        #     vi[wy] = vi[now] + 1
        #     if not board[wy]:
        #         Q.append(wy)
        #     else:
        #         vi[board[wy]] = vi[now] + 1
        #         Q.append(board[wy])
print(vi[-1] - 1)
