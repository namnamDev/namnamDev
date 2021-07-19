import sys

sys.stdin = open('Baekjoon14503.txt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dry = [-1, 0, 1, 0]
drx = [0, 1, 0, -1]

run = True
answer = 0
while run:
    if not board[r][c]:
        answer += 1
        board[r][c] = 2
    turns = 0
    ifNot = True
    for i in range(4):
        turns += 1
        d -= 1
        if d < 0:
            d = 3
        wy = r + dry[d]
        wx = c + drx[d]
        if 0 <= wy < N and 0 <= wx < M and not board[wy][wx]:
            r = wy
            c = wx
            ifNot = False
            break

    if ifNot:
        wy = r - dry[d]
        wx = c - drx[d]
        if 0 <= wy < N and 0 <= wx < M and board[wy][wx] == 2:
            r = wy
            c = wx
        else:
            run = False
print(answer)
