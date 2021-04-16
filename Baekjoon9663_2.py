def dfs(now, nums, cnt, board):
    global an
    if cnt == N - 1:
        print()
        for i in board:
            print(i)
        an += 1
        return

    if nums == N:
        return
    else:
        temp_board = [[0] * N for _ in range(N)]
        for i in range(N):
            for g in range(N):
                temp_board[i][g] = board[i][g]

        if not temp_board[now[0]][now[1]]:
            temp_board[now[0]][now[1]] = 2
            for dirs in range(8):
                wy = now[0] + diry[dirs]
                wx = now[1] + dirx[dirs]
                while 0 <= wy < N and 0 <= wx < N:
                    temp_board[wy][wx] = 1
                    wy += diry[dirs]
                    wx += dirx[dirs]
            temparr = temp_board[nums + 1]
            for i in range(N):
                if not temparr[i]:
                    dfs([nums + 1, i], nums + 1, cnt + 1, temp_board)
            # for i in range(nums + 1, N):
            #     for g in range(N):
            #         if not temp_board[i][g]:
            #             dfs([i, g], nums + 1, cnt + 1, temp_board)
            # dfs([i, g], nums + 1, cnt, board)


diry = [-1, 1, -1, 1, 0, 0, 1, -1]
dirx = [-1, 1, 1, -1, 1, -1, 0, 0]
N = int(input())
an = 0
for i in range(N):
    for g in range(N):
        board_arr = [[0] * N for _ in range(N)]
        dfs([i, g], 0, 0, board_arr)

print(an)
