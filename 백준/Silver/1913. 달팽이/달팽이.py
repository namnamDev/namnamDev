size, target = int(input()), int(input())
board = [[0] * size for _ in range(size)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
mid = size // 2
board[mid][mid] = 1
target_point = [mid + 1, mid + 1]
now = [mid, mid]
now_direction = 3
for i in range(2, size ** 2 + 1):
    dy = now[0] + direction[(now_direction + 1) % 4][0]
    dx = now[1] + direction[(now_direction + 1) % 4][1]
    if not board[dy][dx]:
        board[dy][dx] = i
        now_direction = (now_direction + 1) % 4
        now = [dy, dx]
    else:
        wy = now[0] + direction[now_direction][0]
        wx = now[1] + direction[now_direction][1]
        board[wy][wx] = i
        now = [wy, wx]
    if i == target:
        target_point = [now[0] + 1, now[1] + 1]

for i in board:
    print(*i)

print(*target_point)
