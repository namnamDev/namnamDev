import sys

sys.stdin = open("ExpertAcademy1861.txt")

diry = [1, -1, 0, 0]
dirx = [0, 0, 1, -1]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visitied = [[0] * N for _ in range(N)]
    max_cnt = 0
    min_num = N ** 2
    for i in range(N):
        for g in range(N):
            if not visitied[i][g]:
                Q = [[i, g]]
                cnt = 1
                while len(Q):
                    idx = Q.pop()
                    temp = arr[idx[0]][idx[1]]
                    for drs in range(4):
                        wy = idx[0] + diry[drs]
                        wx = idx[1] + dirx[drs]
                        if 0 <= wy < N and 0 <= wx < N:
                            if arr[wy][wx] == temp + 1:
                                visitied[wy][wx] = visitied[idx[0]][idx[1]] + 1
                                Q.append([wy, wx])
                                cnt += 1
                if cnt:
                    if max_cnt < cnt:
                        max_cnt = cnt
                        min_num = arr[i][g]
                    elif max_cnt == cnt:
                        min_num = min(min_num, arr[i][g])

    print("#{} {} {}".format(tc + 1, min_num, max_cnt))
# 1 6 8
# 2 3 2
# 3 149 2
# 4 2 45
# 5 2 23
# 6 1 2
# 7 1 4
# 8 5 17
# 9 4 2
# 10 1 35
# 11 2 2
# 12 7 2
# 13 45 2
# 14 113 2
# 15 12 32
# 16 6 9
# 17 1 4
# 18 36 42
# 19 204 2
# 20 7 14
# 21 4 2
# 22 8225 2200
# 23 35 3 #
# 24 2 2
# 25 613 2
# 26 33 2
# 27 5 5
