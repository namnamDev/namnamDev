from collections import deque


def star_position(p_building, p_r, p_c, p_l):
    for z in range(p_l):
        for y in range(p_r):
            for x in range(p_c):
                if p_building[z][y][x] == 'S':
                    return [z, y, x]
    return [-1, -1]


dry = [-1, 1, 0, 0, 0, 0]
drx = [0, 0, -1, 1, 0, 0]
drz = [0, 0, 0, 0, 1, -1]
while True:
    L, R, C = map(int, input().split())
    if not (L and R and C):
        break

    building = []
    visit = [[[0] * C for _ in range(R)] for _ in range(L)]

    for _ in range(L):
        building.append([list(input()) for _ in range(R)])
        input()

    now = star_position(building, R, C, L)
    visit[now[0]][now[1]][now[2]] = 1
    movement = deque([now])
    answer = 0
    while movement:
        now = movement.popleft()
        if building[now[0]][now[1]][now[2]] == 'E':
            answer = visit[now[0]][now[1]][now[2]] - 1
            break

        for direction in range(6):
            wz = now[0] + drz[direction]
            wy = now[1] + dry[direction]
            wx = now[2] + drx[direction]

            if 0 <= wz < L and 0 <= wy < R and 0 <= wx < C and not visit[wz][wy][wx] and building[wz][wy][
                wx] != "#":
                visit[wz][wy][wx] = visit[now[0]][now[1]][now[2]] + 1
                movement.append([wz, wy, wx])
    if answer:
        print("Escaped in " + str(answer) + " minute(s).")
    else:
        print("Trapped!")
