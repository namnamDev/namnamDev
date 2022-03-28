import sys

sys.stdin = open("Baekjoon2447.txt")
n = int(input())


def lec(pa_n, p_sx, p_sy):
    if pa_n <= 3:
        board[p_sy + 1][p_sx + 1] = " "
        return
    t = pa_n // 3
    sx_white, sy_white = t + p_sx, t + p_sy
    ex_white, ey_white = t * 2 + p_sx, t * 2 + p_sy
    for y in range(sy_white, ey_white):
        for x in range(sx_white, ex_white):
            board[y][x] = " "
    for d in range(8):
        lec(t, p_sx + div_x[d] * t, p_sy + div_y[d] * t)


div_x = [0, 1, 2, 0, 2, 0, 1, 2]
div_y = [0, 0, 0, 1, 1, 2, 2, 2]
board = [["*"] * n for _ in range(n)]
lec(n, 0, 0)

for i in board:
    print("".join(i))
