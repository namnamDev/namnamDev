import sys
from collections import deque

sys.stdin = open("Baekjoon7562.txt")
diry = [-2, -1, 1, 2, 1, 2, -2, -1]
dirx = [-1, -2, 2, 1, -2, -1, 1, 2]
for tc in range(int(input())):
    size = int(input())
    start = list(map(int, input().split()))
    flag = list(map(int, input().split()))
    Q = deque([start])
    board = [[0] * size for _ in range(size)]
    board[start[0]][start[1]] = 1
    while Q:
        now = Q.popleft()
        for i in range(8):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < size and 0 <= wx < size and not board[wy][wx]:
                board[wy][wx] = 1 + board[now[0]][now[1]]
                Q.append([wy, wx])
                if board[flag[0]][flag[1]]:
                    Q = []
                    break
    print(board[flag[0]][flag[1]] - 1)
