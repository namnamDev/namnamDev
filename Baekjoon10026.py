import sys

sys.stdin = open('Baekjoon10026.txt')
from collections import deque


def bfs(div):
    cnt = 0
    vi = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not vi[y][x]:
                cnt += 1
                if div:  # 1 = 색약 0 = 일반
                    if board[y][x] != "B":
                        nowColor = ["G", "R"]
                    else:
                        nowColor = ["B"]
                else:
                    nowColor = [board[y][x]]
                vi[y][x] = 1
                Q = deque([[y, x]])
                while Q:
                    now = Q.popleft()
                    for d in range(4):
                        wy = now[0] + diry[d]
                        wx = now[1] + dirx[d]
                        if 0 <= wy < N and 0 <= wx < N and (board[wy][wx] in nowColor) and not vi[wy][wx]:
                            vi[wy][wx] = 1
                            Q.append([wy, wx])
    return cnt


diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
N = int(input())
board = [list(input()) for _ in range(N)]
an1 = str(bfs(0))
an2 = str(bfs(1))
print(an1 + " " + an2)
