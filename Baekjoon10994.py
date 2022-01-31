import sys

sys.stdin = open('Baekjoon10994.txt')


def ch(start, end):
    if start > end:
        return
    for x in range(start, end):
        board[start][x] = "*"
        board[end - 1][x] = "*"
        board[x][start] = "*"
        board[x][end - 1] = "*"
    ch(start + 2, end - 2)
    return


n = int(input())
s = n * 4 - 3
board = [[" "] * s for _ in range(s)]
ch(0, s)
for i in board:
    a = ""
    for x in i:
        a += x
    print(a)
