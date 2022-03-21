import sys

sys.stdin = open("Baekjoon16946.txt")
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
Q_1 = deque([])
vi = [[0] * M for _ in range(N)]

counts = {}
count = 1
dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]
for y in range(N):
    for x in range(M):
        if board[y][x]:
            Q_1.append([y, x])
        else:
            if not vi[y][x]:
                vi[y][x] = count
                Q_0 = deque([[y, x]])
                t_count = 0
                while Q_0:
                    y, x, = Q_0.popleft()
                    t_count += 1
                    for d in range(4):
                        wy = y + dry[d]
                        wx = x + drx[d]
                        if 0 <= wy < N and 0 <= wx < M and (not vi[wy][wx]) and (not board[wy][wx]):
                            Q_0.append([wy, wx])
                            vi[wy][wx] = count
                counts[count] = t_count
                count += 1
# print(counts)
# for i in vi:
#     print(i)
while Q_1:
    y, x = Q_1.popleft()
    around_list = []
    around_sum = 1
    for d in range(4):
        wy = y + dry[d]
        wx = x + drx[d]
        if 0 <= wy < N and 0 <= wx < M and vi[wy][wx]:
            around_list.append(vi[wy][wx])
    around_list = list(set(around_list))
    # print(around_list)
    for a in around_list:
        around_sum += counts[a]
    board[y][x] = around_sum % 10

for i in board:
    print("".join(map(str, i)))
