import sys

sys.stdin = open('Baekjoon1012.txt')
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
for tc in range(int(input())):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    S = []
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    cnt = 0

    for f in range(N):
        for g in range(M):
            if board[f][g]:
                cnt += 1
                S = [[f, g]]
                while len(S):
                    now = S.pop()
                    for i in range(4):
                        wy = now[0] + diry[i]
                        wx = now[1] + dirx[i]
                        if 0 <= wy < N and 0 <= wx < M and board[wy][wx]:
                            board[wy][wx] = 0
                            S.append([wy, wx])
    print(cnt)
