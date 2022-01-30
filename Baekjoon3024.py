import sys

sys.stdin = open("Baekjoon3024.txt")


def aa():
    for y in range(a):
        for x in range(a):
            if board[y][x] != ".":
                temp = board[y][x]
                for d in range(4):
                    cnt = 0
                    wy = y + dy[d]
                    wx = x + dx[d]
                    while 0 <= wy < a and 0 <= wx < a and board[wy][wx] == temp:
                        wy += dy[d]
                        wx += dx[d]
                        cnt += 1
                    if cnt == 2:
                        return temp
    return "ongoing"


a = int(input())
board = [list(input()) for _ in range(a)]
dy = [1, 0, 1, -1]
dx = [0, 1, 1, 1]
print(aa())
