def dfs(now, nums, cnt):
    global an
    if cnt == N - 1:
        for i in board:
            print(i)
        an += 1
        return

    if nums == N:
        return
    else:
        dfs(now, nums + 1, cnt)
        print()
        for i in board:
            print(i)
        for i in range(N):
            for g in range(N):
                if not board[i][g]:
                    board[i][g] = 2
                    for dirs in range(8):
                        wy = i + diry[dirs]
                        wx = g + dirx[dirs]
                        while 0 <= wy < N and 0 <= wx < N:
                            board[wy][wx] = 1
                            wy += diry[dirs]
                            wx += dirx[dirs]
                    dfs([i, g], nums + 1, cnt + 1)

        # if not board[now[0]][now[1]]:
        #     board[now[0]][now[1]] = 2
        #     for dirs in range(8):
        #         wy = now[0] + diry[dirs]
        #         wx = now[1] + dirx[dirs]
        #         while 0 <= wy < N and 0 <= wx < N:
        #             board[wy][wx] = 1
        #             wy += diry[dirs]
        #             wx += dirx[dirs]
        # print(nums)
        # for i in board:
        #     print(i)


diry = [-1, 1, -1, 1, 0, 0, 1, -1]
dirx = [-1, 1, 1, -1, 1, -1, 0, 0]
N = int(input())
an = 0
for i in range(N):
    for g in range(N):
        board = [[0] * N for _ in range(N)]
        dfs([i, g], 0, 0)

print(an)
