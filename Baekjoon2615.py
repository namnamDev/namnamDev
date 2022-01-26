import sys

sys.stdin = open("Baekjoon2615.txt")


def oh():
    for x in range(19):
        for y in range(19):
            if board[y][x]:
                col = board[y][x]
                for d in range(8):
                    wy = dy[d] + y
                    wx = dx[d] + x
                    cnt = 1
                    while 0 <= wy < 19 and 0 <= wx < 19 and board[wy][wx] == col:
                        cnt += 1
                        wy += dy[d]
                        wx += dx[d]
                    wwy = y - dy[d]
                    wwx = x - dx[d]
                    while 0 <= wwy < 19 and 0 <= wwx < 19 and board[wwy][wwx] == col:
                        cnt += 1
                        wwy -= dy[d]
                        wwx -= dx[d]
                    if cnt == 5:
                        print(col)
                        print(y + 1, x + 1)
                        return
    print(0)


board = [list(map(int, input().split())) for _ in range(19)]
dy = [-1, 1, 0, 0, 1, 1, -1, - 1]
dx = [1, -1, 1, -1, 0, 1, 0, -1]
oh()
