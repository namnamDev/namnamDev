import sys

sys.stdin = open("Baekjoon1780.txt")


def check(start, end):
    sy, sx = start[0], start[1]
    ey, ex = end[0], end[1]
    temp = board[sy][sx]
    for y in range(sy, ey):
        for x in range(sx, ex):
            if temp != board[y][x]:
                return [0, 0]
    return [1, temp]


def bin(paN, start, end):
    if paN == 1:
        vi[board[start[0]][start[1]]] += 1
        return
    checked = check(start, end)
    if not checked[0]:  # [00][88]
        tempN = paN // 3
        for yy in range(start[0], end[0], tempN):
            for xx in range(start[1], end[1], tempN):
                bin(tempN, [yy, xx], [yy + tempN, xx + tempN])

    else:
        vi[checked[1]] += 1


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
vi = {-1: 0, 0: 0, 1: 0}
bin(N, [0, 0], [N, N])
print(vi[-1])
print(vi[0])
print(vi[1])
