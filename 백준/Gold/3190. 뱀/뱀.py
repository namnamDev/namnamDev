from collections import deque

N = int(input())  # 보드크기
K = int(input())  # 사과 개수
board = [[0] * N for _ in range(N)]
board[0][0] = 1
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2
L = int(input())
l_list = [list(input().split()) for _ in range(L)]
body = deque([[0, 0]])

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     -1 0
# 0 -1   0 1
#     1 0
now_d = 0
t = 0
idx = 0
while True:
    t += 1
    ny, nx = body[-1]
    dy, dx = direction[now_d]
    wy = ny + dy
    wx = nx + dx
    if 0 <= wy < N and 0 <= wx < N and (not board[wy][wx] or board[wy][wx] == 2):
        body.append([wy, wx])
        if not board[wy][wx]:
            t_y, t_x = body.popleft()
            board[t_y][t_x] = 0
        board[wy][wx] = 1
    else:
        print(t)
        break
    if idx < len(l_list):
        if int(l_list[idx][0]) == t:
            if l_list[idx][1] == "D":
                now_d = (now_d + 1) % 4
            else:
                now_d = (now_d - 1) % 4 if now_d else 3
            idx += 1
