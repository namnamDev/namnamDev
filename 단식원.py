import sys

sys.stdin = open("단식원.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]


def recul(depth, br, vis):
    if depth == 3:
        print('--------')
        global an
        tempch = []
        #         # tempbo = [[0] * M for _ in range(N)]
        #         # tempvi = [[0] * M for _ in range(N)]
        #         # cnt = 0
        for i in chicks:
            tempch.append(i)
        # for i in range(N):
        #     for g in range(M):
        #         tempbo[i][g] = board[i][g]
        #         tempvi[i][g] = vi[i][g]
        print(tempch)
        while tempch:
            now = tempch.pop()
            for i in range(4):
                wy = diry[i] + now[0]
                wx = dirx[i] + now[1]
                if 0 <= wy < N and 0 <= wx < M:
                    if vis[wy][wx] == 0:
                        vis[wy][wx] = 1
                        br[wy][wx] = 2
                        tempch.append([wy, wx])
        cnt = 0
        for i in range(N):
            print(br[i])
            for g in range(M):
                if not br[i][g]:
                    cnt += 1
        tempan = an
        an = max(cnt, an)
        if tempan != an:
            print('--------')
            for i in br:
                print(i)
                print(an)
        return
    else:
        for i in range(N):
            for g in range(M):
                if vis[i][g] == 0 and br[i][g] == 0:
                    vis[i][g] = 1
                    br[i][g] = 1
                    recul(depth + 1, br, vis)
                    vis[i][g] = 0
                    br[i][g] = 0


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
    recul(0, board, vi)
    print("#{} {}".format(tc + 1, an))
    for i in board:
        print(i)
