import sys

sys.stdin = open("Baekjoon1992.txt")


def check(xs, xe, ys, ye):
    temp = board[ys][xs]
    for y in range(ys, ye):
        for x in range(xs, xe):
            if temp != board[y][x]:
                return False

    return True


def rec(xs, ys, idx):
    global an
    if not idx:
        an += str(board[ys][xs])
        return
    if check(xs, xs + 2 ** idx, ys, ys + 2 ** idx):
        an += str(board[ys][xs])
        return
    an += "("
    ti = idx - 1
    rec(xs, ys, ti)
    rec(xs + 2 ** ti, ys, ti)
    rec(xs, ys + 2 ** ti, ti)
    rec(xs + 2 ** ti, ys + 2 ** ti, ti)
    an += ")"


n = int(input())
board = [list(map(int, input())) for _ in range(n)]
an = ""
cnt = 0
while 2 ** cnt < n:
    cnt += 1
rec(0, 0, cnt)
print(an)
