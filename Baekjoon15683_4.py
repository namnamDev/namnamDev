import sys

sys.stdin = open("Baekjoon15683.txt")


def p(arr):
    if len(arr) == len(Q):
        tb = [[0] * M for _ in range(N)]
        for ff in range(N):
            for gg in range(M):
                tb[ff][gg] = b[ff][gg]

        for nums in range(len(arr)):
            now = Q[nums]

            nowdir = ds[now[2]][arr[nums]]
            for ff in nowdir:
                wy = now[0] + ff[0]
                wx = now[1] + ff[1]
                while 0 <= wy < N and 0 <= wx < M:
                    if tb[wy][wx] == 0:
                        tb[wy][wx] = 7
                    elif tb[wy][wx] == 6:
                        break
                    wy += ff[0]
                    wx += ff[1]
        z = 0
        for i in tb:
            z += i.count(0)
        global ms
        if z < ms:
            ms = z
        return
    else:
        now = Q[len(arr)]
        for i in range(len(ds[now[2]])):
            p(arr + [i])


N, M = map(int, input().split())
d1 = [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]]
d2 = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]]
d3 = [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
d4 = [[[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]], [[0, -1], [-1, 0], [0, 1]]]
d5 = [[[0, 1], [0, -1], [1, 0], [-1, 0]]]
ds = [d1, d2, d3, d4, d5]
b = [list(map(int, input().split())) for _ in range(N)]
Q = []
for i in range(N):
    for g in range(M):
        if 0 < b[i][g] < 6:
            Q.append([i, g, b[i][g] - 1])

ms = N * M
p([])
print(ms)
