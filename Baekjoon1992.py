import sys

sys.stdin = open("Baekjoon1992.txt")


def check(xs, xe, ys, ye):
    temp = board[xs][ys]
    for y in range(ys, ye):
        for x in range(xs, xe):
            if temp != board[y][x]:
                return False
    return True


def rec(xs, xe, ys, ye):
    global an
    if xs >= xe or ys >= ye:
        # an += str(board[xs][ys])
        print("pass")
        return
    print(xs, xe, ys, ye)
    if check(xs, xe, ys, ye):
        an += str(board[xs][ys])
    else:
        an += "("
        rec(xs, xe // 2, ys, ye // 2)  # 8 // 2 -- 4
        rec(xe // 2 + 1, xe, ys, ye // 2)  # 5 // 2
        rec(xs, xe // 2, ye // 2 + 1, ye)
        rec(xe // 2 + 1, xe, ye // 2 + 1, ye)
        an += ")"


n = int(input())
board = [list(map(int, input())) for _ in range(n)]
an = ""
for i in board:
    print(i)
print()
rec(0, n - 1, 0, n - 1)
print(an)
