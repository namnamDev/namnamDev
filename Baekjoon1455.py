import sys

sys.stdin = open("Baekjoon1455.txt")
a, b = map(int, input().split())
board = [list(map(int, input())) for _ in range(a)]
cnt = 0
for yy in range(a - 1, -1, -1):
    for xx in range(b - 1, -1, -1):
        if board[yy][xx]:
            for y in range(yy + 1):
                for x in range(xx + 1):
                    board[y][x] = 1 - board[y][x]
            cnt += 1
print(cnt)
