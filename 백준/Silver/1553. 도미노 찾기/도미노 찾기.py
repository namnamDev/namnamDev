arr = [list(input()) for _ in range(8)]

board = [["7"] * 7 for _ in range(8)]
visit = [0] * 28


def lec(pidx):
    if pidx == 28:
        global an
        an += 1
        return
    domino = dominos[pidx]
    for y in range(8):
        for x in range(7):
            if board[y][x] == "7":
                temp = domino
                if x + 1 < 7 and board[y][x + 1] == "7":
                    if temp[0] == arr[y][x] and temp[1] == arr[y][x + 1]:
                        board[y][x] = temp[0]
                        board[y][x + 1] = temp[1]
                        lec(pidx + 1)
                        board[y][x] = board[y][x + 1] = "7"

                if y + 1 < 8 and board[y + 1][x] == "7":
                    if temp[0] == arr[y][x] and temp[1] == arr[y + 1][x]:
                        board[y][x] = temp[0]
                        board[y + 1][x] = temp[1]
                        lec(pidx + 1)
                        board[y][x] = board[y + 1][x] = "7"
                if temp[0] != temp[1]:
                    temp = temp[::-1]
                    if x + 1 < 7 and board[y][x + 1] == "7":
                        if temp[0] == arr[y][x] and temp[1] == arr[y][x + 1]:
                            board[y][x] = temp[0]
                            board[y][x + 1] = temp[1]
                            lec(pidx + 1)
                            board[y][x] = board[y][x + 1] = "7"

                    if y + 1 < 8 and board[y + 1][x] == "7":
                        if temp[0] == arr[y][x] and temp[1] == arr[y + 1][x]:
                            board[y][x] = temp[0]
                            board[y + 1][x] = temp[1]
                            lec(pidx + 1)
                            board[y][x] = board[y + 1][x] = "7"


dominos = []
for i in range(7):
    for f in range(i, 7):
        dominos.append([str(i), str(f)])
an = 0
lec(0)
print(an)
