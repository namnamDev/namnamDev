import sys
from collections import deque

sys.stdin = open('Baekjoon1987.txt')


def dfs(ny, nx, arr):
    global length
    cnt = 0
    for d in range(4):
        wy = ny + diry[d]
        wx = nx + dirx[d]
        if 0 <= wy < R and 0 <= wx < C and board[wy][wx] not in arr:
            dfs(wy, wx, arr + board[wy][wx])
        else:  # 움직일수 없는 경우 체크
            cnt += 1
    if cnt == 4:  # 움직일수 없는경우가 4가지일떄 == 못움직일때
        length += [len(arr)]
        return


diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
length = []
dfs(0, 0, board[0][0])
print(max(length))
