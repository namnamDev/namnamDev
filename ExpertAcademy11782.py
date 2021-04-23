import sys
from collections import deque

sys.stdin = open('ExpertAcademy11782.txt')
dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]


def dfs(y, x):
    global min_road
    if vi[y][x] > min_road:
        return
    if vi[N - 1][N - 1]:
        print()
        for i in vi:
            print(i)
        min_road = min(vi[N - 1][N - 1], min_road)
        return
    for dr in range(4):
        wy = y + dry[dr]
        wx = x + drx[dr]
        if 0 <= wy < N and 0 <= wx < N:
            if not vi[wy][wx]:
                temp = board[wy][wx] - board[y][x] if board[wy][wx] > board[y][x] else 0
                vi[wy][wx] = vi[y][x] + 1 + temp
                dfs(wy, wx)
                vi[wy][wx] = 0


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    vi = [[0] * N for _ in range(N)]
    vi[0][0] = 1
    min_road = 9999999999
    dfs(0, 0)
    print("#{} {}".format(tc + 1, min_road))
