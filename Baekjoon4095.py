import sys

sys.stdin = open("Baekjoon4095.txt")
while True:
    N, M = map(int, input().split())
    if not (N and M):
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in board:
        print(i)
    an = 0
    y = x = 0
    while y < N - an:
        while x < M - an:
            if board[y][x]:
                wy = y
                wx = x
                while wy < N and wx < N and board[wy][x] and board[y][wx]:
                    wy += 1
                    wx += 1
            x += 1
        print(an)
        y += 1
    print(an)
    # for y in range(M):
    #     for x in range(N):
    #         if board[y][x]:
    #             pass
