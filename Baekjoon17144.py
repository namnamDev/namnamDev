import sys

sys.stdin = open("Baekjoon17144.txt")
from collections import deque

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque([])
air_fresher = []
for y in range(R):
    for x in range(C):
        if board[y][x] > 0:
            Q.append([y, x])
        elif board[y][x] < 0:
            air_fresher.append([y, x])
# 미세먼지 확장
time = 0
while time < T:
    temp_board = [[0] * C for _ in range(R)]
    vi = [[0] * C for _ in range(R)]
    Q2 = deque([])
    for y in range(R):
        for x in range(C):
            temp_board[y][x] = board[y][x]
            if board[y][x] > 0:
                Q2.append([y, x])
    # Q2 = Q.copy()
    Q.clear()
    # print("before", Q2)
    # for i in range(C):
    #     print(board[i], temp_board[i])
    while len(Q2):
        y, x = Q2.popleft()
        vi[y][x] = 1
        dirs = []
        for d in range(4):
            wy = dy[d] + y
            wx = dx[d] + x
            if 0 <= wy < R and 0 <= wx < C and board[wy][wx] >= 0:
                dirs.append([wy, wx])
                if not vi[wy][wx]:
                    vi[wy][wx] = 1
                    Q.append([wy, wx])
        div = len(dirs)
        center_v = temp_board[y][x]
        around_v = temp_board[y][x] // 5
        board[y][x] -= around_v * div
        # print(Q)
        # print(Q2)
        # print(y, x, dirs)
        for t_dy, t_dx in dirs:
            board[t_dy][t_dx] += around_v
        # print(board[y][x], around_v * div)
        # print("after")
        # for s in range(R):
        #     print(board[s])

    # 공기청정기 작동
    air_top_y, air_top_x = air_fresher[0]
    air_bot_y, air_bot_x = air_fresher[1]
    t_x = air_top_x + 1
    air_top_line = []
    while t_x < C - 1:
        air_top_line.append([board[air_top_y][t_x], air_top_y, t_x])
        t_x += 1
    t_y = air_top_y
    while t_y > 0:
        air_top_line.append([board[t_y][C - 1], t_y, C - 1])
        t_y -= 1
    t_x = C - 1
    while t_x > 0:
        air_top_line.append([board[0][t_x], 0, t_x])
        t_x -= 1
    t_y = 0
    while t_y < air_top_y:
        air_top_line.append([board[t_y][0], t_y, 0])
        t_y += 1
    board[air_top_line[0][1]][air_top_line[0][2]] = 0
    for tt in range(1, len(air_top_line)):
        board[air_top_line[tt][1]][air_top_line[tt][2]] = air_top_line[tt - 1][0]

    air_bot_line = []
    t_x = air_bot_x + 1
    while t_x < C - 1:
        air_bot_line.append([board[air_bot_y][t_x], air_bot_y, t_x])
        t_x += 1

    t_y = air_bot_y
    while t_y < R - 1:
        air_bot_line.append([board[t_y][C - 1], t_y, C - 1])
        t_y += 1

    t_x = C - 1
    while t_x > 0:
        air_bot_line.append([board[R - 1][t_x], R - 1, t_x])
        t_x -= 1

    t_y = R - 1
    while t_y > air_bot_y:
        air_bot_line.append([board[t_y][0], t_y, 0])
        t_y -= 1
    board[air_bot_line[0][1]][air_bot_line[0][2]] = 0
    for tt in range(1, len(air_bot_line)):
        board[air_bot_line[tt][1]][air_bot_line[tt][2]] = air_bot_line[tt - 1][0]
    time += 1
    t_answer = 2
    # print("turn")
    # for i in range(R):
    #     print(board[i])
    # for i in board:
    #     t_answer += sum(i)
    # print(time, t_answer)
answer = 2
for i in board:
    answer += sum(i)
print(answer)
