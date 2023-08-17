from collections import deque


def my_combination(depth, arr, size):
    if len(arr) == 5:
        floor_combination.append(arr)
        return
    if depth == 5:
        return

    for i in range(size):
        if not visit[i]:
            visit[i] = 1
            my_combination(depth + 1, arr + [i], size)
            visit[i] = 0


def my_turn_combination(depth, arr, size):
    if depth == 5:
        turn_combination.append(arr)
        return

    for i in range(4):
        my_turn_combination(depth + 1, arr + [i], size)


def turn_board(par_board):
    temp_board = [[0] * 5 for _ in range(5)]
    for up in range(5):
        temp_board[up][4] = par_board[0][up]

    for right in range(5):
        temp_board[4][4 - right] = par_board[right][4]

    for bottom in range(5):
        temp_board[4 - bottom][0] = par_board[4][4 - bottom]

    for left in range(5):
        temp_board[0][left] = par_board[4 - left][0]

    for up in range(1, 4):
        temp_board[up][3] = par_board[1][up]

    for right in range(1, 4):
        temp_board[3][4 - right] = par_board[right][3]

    for bottom in range(1, 4):
        temp_board[4 - bottom][1] = par_board[3][4 - bottom]

    for left in range(1, 4):
        temp_board[1][left] = par_board[4 - left][1]

    temp_board[2][2] = par_board[2][2]
    return temp_board


## 00 01 02 03 04 -> 04 14 24 34 44
## 04 14 24 34 44 -> 44 43 42 41 40
## 44 43 42 41 40 -> 40 30 20 10 00
## 40 30 20 10 00 -> 00 01 02 03 04

## 11 12 13 -> 13 23 33
## 13 23 33 -> 33 32 31
## 33 32 31 -> 31 21 11
## 31 21 11 -> 11 12 13

cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

visit = [0] * 5
floor_combination = []
turn_combination = []
my_combination(0, [], 5)
my_turn_combination(0, [], 4)
memo_board_list = []

for floor in cube:
    temp_floor = floor
    temp_list = []
    for _ in range(4):
        turned_board = turn_board(temp_floor)
        temp_list.append(turned_board)
        temp_floor = turned_board

    memo_board_list.append(temp_list)


def my_lec(floor_com, turn_com, now_loc, moved_cnt):
    global answer
    if moved_cnt >= answer:
        return
    if now_loc[0] == 4:
        if now_loc == [4, 4, 4]:
            answer = min(answer, moved_cnt)
        return

    for direc in range(6):
        wz = now_loc[0] + drz[direc]
        wy = now_loc[1] + dry[direc]
        wx = now_loc[2] + drx[direc]
        if 0 <= wz < 5 and 0 <= wy < 5 and 0 <= wx < 5:
            if memo_board_list[floor_com[wz]][turn_com[wz]][wy][wx] and not visit[wz][wy][wx]:
                visit[wz][wy][wx] = 1
                my_lec(floor_com, turn_com, [wz, wy, wx], moved_cnt + 1)
                visit[wz][wy][wx] = 0


drz = [1, -1, 0, 0, 0, 0]
dry = [0, 0, -1, 1, 0, 0]
drx = [0, 0, 0, 0, -1, 1]

answer = 99999999999999999999
for c in floor_combination:
    for turn_c in turn_combination:
        if memo_board_list[c[0]][turn_c[0]][0][0]:
            visit = [[[0] * 5 for _ in range(5)] for _ in range(5)]
            visit[0][0][0] = 1
            Q = deque([[0, 0, 0]])
            while Q:
                nz, ny, nx = map(int, Q.popleft())
                if visit[4][4][4]:
                    answer = min(answer, visit[4][4][4])
                    break

                for d in range(6):
                    wz = nz + drz[d]
                    wy = ny + dry[d]
                    wx = nx + drx[d]
                    if 0 <= wz < 5 and 0 <= wy < 5 and 0 <= wx < 5:
                        if memo_board_list[c[wz]][turn_c[wz]][wy][wx] and not visit[wz][wy][wx]:
                            visit[wz][wy][wx] = 1 + visit[nz][ny][nx]
                            Q.append([wz, wy, wx])

if answer == 99999999999999999999:
    print(-1)
else:
    print(answer - 1)