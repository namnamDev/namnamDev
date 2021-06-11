import sys
from collections import deque

sys.stdin = open('좀비아파트를구하라.txt')

dirz = [-1, 1, 0, 0, 0, 0]
diry = [0, 0, -1, 1, 0, 0]
dirx = [0, 0, 0, 0, -1, 1]


def check(cnt):
    temp = 0
    for i in range(H):
        for g in range(M):
            for f in range(N):
                if apart[i][g][f] == -1:
                    return 'STILL ZOMBIES'
                else:
                    temp += 1
    if not cnt and temp == N * M * H:
        return 'ALL HUMANS'
    return cnt


for tc in range(int(input())):
    N, M, H = map(int, input().split())
    apart = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
    Q = deque([])
    for i in range(H):
        for g in range(M):
            for f in range(N):
                if apart[i][g][f] == 1:
                    Q.append([i, g, f])
    # print(Q)
    cnt = 0
    while Q:
        Q2 = Q
        Q = deque([])
        while Q2:
            now = Q2.popleft()
            for i in range(6):
                wz = now[0] + dirz[i]
                wy = now[1] + diry[i]
                wx = now[2] + dirx[i]
                if 0 <= wz < H and 0 <= wy < M and 0 <= wx < N:
                    if apart[wz][wy][wx] == -1:
                        apart[wz][wy][wx] = 1
                        Q.append([wz, wy, wx])
        cnt += 1
    cnt -= 1
    print("#{} {}".format(tc + 1, check(cnt)))
    # an = ''
    # temp = 0
    # for i in range(H):
    #     for g in range(M):
    #         for f in range(N):
    #             if apart[i][g][f] == -1:
    #                 # print("#{} {}".format(tc + 1, 'STILL ZOMBIES'))
    #                 break
    #             else:
    #                 temp += 1
    # print("#{} {}".format(tc + 1, cnt - 1))
