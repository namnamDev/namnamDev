import sys

sys.stdin = open('Baekjoon14503.txt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(N, M)
print(r, c, d)
dry = [-1, 0, 1, 0]
drx = [0, 1, 0, -1]
for i in board:
    print(i)
run = True
while run:
    board[r][c] = 2
    turns = 0
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3
        wy = r + dry[d]
        wx = c + drx[d]
        if 0 <= wy < N and 0 <= wx < M and not board[wy][wx]:
            turns += 1
            r = wy
            c = wx
            break

        if turns == 4:
            wy = r - dry[d]
            wx = c - drx[d]
            if 0 <= wy < N and 0 <= wx < M and board[wy][wx] == 2:
                r = wy
                c = wx
            else:
                run = False
