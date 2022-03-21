import sys

sys.stdin = open("Baekjoon16234.txt")

from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

days = 0
while True:
    print()
    for i in board:
        print(i)
    vi = [[0] * N for _ in range(N)]
    tot = 0
    for y in range(N):
        for x in range(N):
            if not vi[y][x]:
                temp_list = [[y, x]]
                vi[y][x] = 1
                Q = deque([[y, x]])
                cnt = board[y][x]
                while Q:
                    y, x = Q.popleft()
                    for d in range(4):
                        wy = dy[d] + y
                        wx = dx[d] + x
                        if 0 <= wy < N and 0 <= wx < N and not vi[wy][wx]:
                            # print(L <= abs(board[y][x] - board[wy][wx]) <= R)
                            if L <= abs(board[y][x] - board[wy][wx]) <= R:
                                vi[wy][wx] = 1
                                Q.append([wy, wx])
                                temp_list.append([wy, wx])
                                cnt += board[wy][wx]
                if len(temp_list) == 1:
                    tot += 1
                else:
                    val = cnt // len(temp_list)
                    for ty, tx in temp_list:
                        board[ty][tx] = val
    if tot == N * N:
        print(days)
        break
    days += 1
