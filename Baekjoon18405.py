import sys

sys.stdin = open("Baekjoon18405.txt")


def myIn():
    return map(int, input().split())


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, K = myIn()
board = [list(myIn()) for _ in range(N)]
S, X, Y = myIn()
c = 0

while c < S:
    vi = [[0] * N for _ in range(N)]
    for k in range(1, K + 1):
        for y in range(N):
            for x in range(N):
                if board[y][x] == k and not vi[y][x]:
                    vi[y][x] = 1
                    for d in range(4):
                        wy = y + dy[d]
                        wx = x + dx[d]
                        if 0 <= wy < N and 0 <= wx < N and not board[wy][wx] and not vi[wy][wx]:
                            vi[wy][wx] = 1
                            board[wy][wx] = k
    c += 1
    if board[X - 1][Y - 1]:
        break
print(board[X - 1][Y - 1])
