import sys

sys.stdin = open('Baekjoon16236.txt')
from collections import deque

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
first = []
size = 2
time = 0
for i in range(N):
    for g in range(N):
        if board[i][g] == 9:
            first = [i, g]

Q = deque([first])

eat_cnt = 0
while len(Q):
    eat_point = []
    vi = [[0] * N for _ in range(N)]
    start = [Q[0][0], Q[0][1]]
    vi[start[0]][start[1]] = 1
    while len(Q):
        now = Q.popleft()
        for drs in range(4):
            wy = now[0] + diry[drs]
            wx = now[1] + dirx[drs]
            if 0 <= wy < N and 0 <= wx < N and not vi[wy][wx]:
                if 0 < board[wy][wx] < size:  # 자기와 같거나 작은애들칸만 이동 가능
                    vi[wy][wx] = vi[now[0]][now[1]] + 1
                    eat_point.append([vi[now[0]][now[1]] + 1, wy, wx])
                elif not board[wy][wx] or board[wy][wx] == size:
                    vi[wy][wx] = vi[now[0]][now[1]] + 1
                    Q.append([wy, wx])

    if len(eat_point):
        eat_point.sort()
        y = eat_point[0][1]
        x = eat_point[0][2]
        time += eat_point[0][0] - 1
        eat_cnt += 1
        if eat_cnt == size:
            size += 1
            eat_cnt = 0
        board[y][x] = 9
        board[start[0]][start[1]] = 0
        Q.append([y, x])

print(time)
