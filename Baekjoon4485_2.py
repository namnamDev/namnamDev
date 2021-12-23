import sys

sys.stdin = open('Baekjoon4485.txt')
arrs = []
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
while True:
    N = int(input())
    if not N:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    arrs.append(board)

for tc in range(len(arrs)):
    board = arrs[tc]
    size = len(board)
    vi = [[9999999999] * size for _ in range(size)]
    vi[0][0] = board[0][0]
    Q = [[0, 0]]
    while Q:
        now = Q.pop()
        pay = vi[now[0]][now[1]]
        if pay < vi[-1][-1]:
            for i in range(4):
                wy = now[0] + diry[i]
                wx = now[1] + dirx[i]
                if 0 <= wy < size and 0 <= wx < size and pay + board[wy][wx] < vi[wy][wx]:
                    vi[wy][wx] = pay + board[wy][wx]
                    Q.append([wy, wx])

    print("Problem " + str(tc + 1) + ": " + str(vi[-1][-1]))
