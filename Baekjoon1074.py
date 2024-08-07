import sys

sys.stdin = open("Baekjoon1074.txt")


def recul(n, paY, paX):
    if board[r][c]:
        return
    if n > 1:
        tempN = n - 1
        recul(tempN, paY, paX)
        recul(tempN, paY, paX + 2 ** tempN)
        recul(tempN, paY + 2 ** tempN, paX)
        recul(tempN, paY + 2 ** tempN, paX + 2 ** tempN)
    else:
        global cnt
        for i in range(4):
            wy = paY + diry[i]
            wx = paX + dirx[i]
            board[wy][wx] = cnt
            cnt += 1


diry = [0, 0, 1, 1]
dirx = [0, 1, 0, 1]
N, r, c = map(int, input().split())
print(N, r, c)
board = [[0] * (2 ** N) for _ in range(2 ** N)]
cnt = 0
recul(N, 0, 0)
for line in board:
    print(line)
print(board[r][c])
# n = 1
# [0,0][1,0][0,1][1,1]
# n=2
# 00, 20, 02, 22 >> 00 n**
# 00 10 01 11  >>00
# 20 30 21 31  >>20 + 00 10 01 11
# 02 12 30 13  >>02 + 00 10 01 11
# 22 23 32 33  >>22 + 00 ....
# n=3
# 00 40 04 44
