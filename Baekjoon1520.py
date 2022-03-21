import sys

sys.stdin = open("Baekjoon1520.txt")

from collections import deque

#
# def lec(y, x):
#     global N, M
#     if y == N - 1 and x == M - 1:
#         global cnt
#         cnt += 1
#         return
#     for d in range(4):
#         wy = dy[d] + y
#         wx = dx[d] + x
#         if 0 <= wy < N and 0 <= wx < M and board[wy][wx] < board[y][x]:
#             lec(wy, wx)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
cnt = 0
# vi = [[0] * M for _ in range(N)]
# vi[0][0] = 0
# Q = deque([[0, 0]])
# while Q:
#     y, x = Q.popleft()
#     for d in range(4):
#         wy = dy[d] + y
#         wx = dx[d] + x
#         if 0 <= wy < N and 0 <= wx < M and board[wy][wx] < board[y][x]:
#             vi[wy][wx] += 1
#             Q.append([wy, wx])
# print(vi[-1][-1])
# lec(0, 0)
dp = [[0] * M for _ in range(N)]
for y in range(1, N):
    if board[y][0] < board[y - 1][0]:
        dp[y][0] = 1
    else:
        break
for x in range(1, M):
    if board[0][x] < board[0][x - 1]:
        dp[0][x] = 1
    else:
        break
for y in range(1, N):
    for x in range(1, M):
        if board[y][x] < board[y - 1][x]:
            dp[y][x] += dp[y - 1][x]
        if board[y][x] < board[y][x - 1]:
            dp[y][x] += dp[y][x - 1]
for i in dp:
    print(i)
print(cnt)
