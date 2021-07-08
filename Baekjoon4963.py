import sys

sys.stdin = open("Baekjoon4963.txt")
diry = [-1, 1, -1, 1, 0, 0, 1, -1]
dirx = [-1, 1, 1, -1, -1, 1, 0, 0]
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    vi = [[0] * w for _ in range(h)]

    island = []
    for i in range(h):
        for g in range(w):
            if board[i][g] and not vi[i][g]:
                tempIsland = []
                S = [[i, g]]
                vi[i][g] = 1
                while S:
                    now = S.pop()
                    tempIsland.append(now)
                    for dirs in range(8):
                        wy = diry[dirs] + now[0]
                        wx = dirx[dirs] + now[1]
                        if 0 <= wy < h and 0 <= wx < w and board[wy][wx] and not vi[wy][wx]:
                            vi[wy][wx] = 1
                            S.append([wy, wx])
                island.append(tempIsland)
    print(len(island))
