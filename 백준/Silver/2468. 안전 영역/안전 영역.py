N = int(input())
board = []
used = {}
used2 = []
for _ in range(N):
    temp = list(map(int, input().split()))
    for one in temp:
        if not used.get(one):
            used[one] = 1
            used2.append(one)
    board.append(temp)
used2.sort(reverse=True)

dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]
max_cnt = 0

used2.append(0)
for hi in used2:
    vi = [[0] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if not vi[y][x] and board[y][x] > hi:
                cnt += 1
                vi[y][x] = cnt
                stack = [[y, x]]
                while stack:
                    ny, nx = stack.pop()
                    for d in range(4):
                        wy = ny + dry[d]
                        wx = nx + drx[d]
                        if 0 <= wy < N and 0 <= wx < N and not vi[wy][wx] and board[wy][wx] > hi:
                            vi[wy][wx] = cnt
                            stack.append([wy, wx])
    max_cnt = max(max_cnt, cnt)
print(max_cnt)