import sys

sys.stdin = open("Baekjoon1890.txt")

from collections import deque

a = int(input())
board = [list(map(int, input().split())) for _ in range(a)]
vi = [[0] * a for _ in range(a)]
dy = [1, 0]
dx = [0, 1]
Q = deque([[0, 0]])
board[-1][-1] = 1

while Q:
    now = Q.popleft()
    print(now)
    t = board[now[0]][now[1]]
    dy = [t, 0]
    dx = [0, t]
    for i in range(2):
        wy = dy[i] + now[0]
        wx = dx[i] + now[1]
        if 0 <= wy < a and 0 <= wx < a:
            vi[wy][wx] += 1
            Q.append([wy, wx])
print(vi[-1][-1])
for v in vi:
    print(v)
