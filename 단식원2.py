import sys

sys.stdin = open("단식원.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]


def recul(depth, n, m):
    if depth == 3:

        global an
        tempch = []
        tempbo = [[0] * M for _ in range(N)]
        tempvi = [[0] * M for _ in range(N)]
        cnt = 0
        for i in chicks:
            tempch.append(i)
        for i in range(N):
            for g in range(M):
                tempbo[i][g] = board[i][g]
                tempvi[i][g] = vi[i][g]
        while tempch:
            now = tempch.pop()
            for i in range(4):
                wy = diry[i] + now[0]
                wx = dirx[i] + now[1]
                if 0 <= wy < N and 0 <= wx < M:
                    if tempvi[wy][wx] == 0:
                        tempvi[wy][wx] = 1
                        tempbo[wy][wx] = 2
                        tempch.append([wy, wx])
        for i in range(N):

            for g in range(M):
                if not tempbo[i][g]:
                    cnt += 1
        tempan = an
        an = max(cnt, an)
        # print('------')
        # for i in tempbo:
        #     print(i)
        # print(an)
        # if tempan != an:
        # print('------')
        # for i in tempbo:
        #     print(i)
        return
    else:
        for i in range(n, N):
            for g in range(M):
                if vi[i][g] == 0 and board[i][g] == 0:
                    vi[i][g] = 1
                    board[i][g] = 1
                    recul(depth + 1, i, g)
                    vi[i][g] = 0
                    board[i][g] = 0


for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    vi = [[0] * M for _ in range(N)]
    chicks = []
    for i in range(N):
        for g in range(M):
            if board[i][g] == 2:
                vi[i][g] = 2
                chicks.append([i, g])
            elif board[i][g] == 1:
                vi[i][g] = 1
    an = 0
    arr = {}
    recul(0, 0, 0)
    print("#{} {}".format(tc + 1, an))
