board = [["."] * 6 for _ in range(6)]
board[2][2] = board[3][3] = "W"
board[2][3] = board[3][2] = "B"
dry = [-1, 1, 0, 0, -1, 1, 1, -1]
drx = [-1, 1, -1, 1, 0, 0, -1, 1]
for tc in range(int(input())):
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    turn = "W" if tc % 2 else "B"
    other = "B" if tc % 2 else "W"
    canDirection = []
    board[y][x] = turn
    for d in range(8):
        wy = y + dry[d]
        wx = x + drx[d]
        while 0 <= wy < 6 and 0 <= wx < 6 and board[wy][wx] != ".":
            if board[wy][wx] == turn:
                canDirection.append(d)
                break
            wy += dry[d]
            wx += drx[d]
    for dIdx in canDirection:
        wy = y + dry[dIdx]
        wx = x + drx[dIdx]
        while 0 <= wy < 6 and 0 <= wx < 6 and board[wy][wx] == other:
            board[wy][wx] = turn
            wy += dry[dIdx]
            wx += drx[dIdx]
for i in board:
    print("".join(i))
wcnt = bcnt = 0
for line in board:
    for one in line:
        if one == "W":
            wcnt += 1
        elif one == "B":
            bcnt += 1
if wcnt > bcnt:
    print("White")
else:
    print("Black")
