import sys

sys.stdin = open("Baekjoon18290.txt")


def ch(paArr):
    if len(paArr) == K:
        global an
        an = max(an, sum(paArr))
        return
    for y in range(N):
        for x in range(M):
            if not vi[y][x]:
                vi[y][x] = 1
                tB = []
                for d in range(4):
                    wy = dy[d] + y
                    wx = dx[d] + x
                    if 0 <= wy < N and 0 <= wx < M and not vi[wy][wx]:
                        tB.append([wy, wx])
                        vi[wy][wx] = 1
                aa = sorted(paArr + [board[y][x]])
                if not c.get(str(aa)):
                    c[str(aa)] = 1
                    ch(paArr + [board[y][x]])
                vi[y][x] = 0
                for i in tB:
                    vi[i[0]][i[1]] = 0


c = {}
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
vi = [[0] * M for _ in range(N)]
an = 0
ch([])
print(an)
