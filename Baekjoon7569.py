# import sys
#
# sys.stdin = open("Baekjoon7569.txt")
#
#
# def start(arr, tenp):
#     result = []
#     for i in range(H):
#         for g in range(N):
#             for h in range(M):
#                 if tenp:
#                     if arr[i][g][h] == tenp:
#                         result.append((i, g, h))
#                 else:
#                     if arr[i][g][h] == tenp:
#                         return True
#     return result
#
#
# dirz = [-1, 1, 0, 0, 0, 0]
# diry = [0, 0, -1, 1, 0, 0]
# dirx = [0, 0, 0, 0, -1, 1]
# M, N, H = map(int, sys.stdin.readline().split())
# arr = [[list(map(int, sys.stdin.readline().split())) for i in range(N)] for h in range(H)]
#
# Q = start(arr, 1)
# Q2 = []
# cnt = 0
# while len(Q) != 0:
#     while len(Q) != 0:
#         now = Q.pop()
#         for i in range(6):
#             wz = now[0] + dirz[i]
#             wy = now[1] + diry[i]
#             wx = now[2] + dirx[i]
#             if 0 <= wz < H and 0 <= wy < N and 0 <= wx < M:
#                 if arr[wz][wy][wx] == 0:
#                     Q2.append((wz, wy, wx))
#                     arr[wz][wy][wx] = 1
#     Q = list(Q2)
#     Q2 = []
#     cnt += 1
# cnt -= 1
# if start(arr, 0):
#     cnt = -1
#
# print(cnt)

import random
