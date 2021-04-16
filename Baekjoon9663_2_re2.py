def dfs(now, nums, cnt, board):
    global an
    if cnt == N - 1:
        an += 1
        return

    if nums == N:
        return
    else:
        
        if not board[now[0]][now[1]]:
            board[now[0]][now[1]] = 2
            for dirs in range(8):
                wy = now[0] + diry[dirs]
                wx = now[1] + dirx[dirs]
                while 0 <= wy < N and 0 <= wx < N:
                    board[wy][wx] = 1
                    wy += diry[dirs]
                    wx += dirx[dirs]
            temparr = board[nums + 1]
            for i in range(N):
                if not temparr[i]:
                    dfs([nums + 1, i], nums + 1, cnt + 1, board)


diry = [-1, 1, -1, 1, 0, 0, 1, -1]
dirx = [-1, 1, 1, -1, 1, -1, 0, 0]
N = int(input())
an = 0
for i in range(N):
    for g in range(N):
        board_arr = [[0] * N for _ in range(N)]
        dfs([i, g], 0, 0, board_arr)

print(an)
