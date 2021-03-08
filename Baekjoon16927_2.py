import sys

sys.stdin = open("Baekjoon16927.txt")

y = [1, 0, -1, 0]
x = [0, 1, 0, -1]
N, M, R = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
for ii in range(N):
    for gg in range(M):
        if v[ii][gg] == 0:
            Q1 = []
            Q2 = []
            s = [ii, gg]
            v[ii][gg] = 1
            Q1.append([ii, gg])
            Q2.append([ii, gg])
            g = 0
            while g != 4:
                wy = s[0] + y[g]
                wx = s[1] + x[g]
                if (0 <= wy < N and 0 <= wx < M) and v[wy][wx] == 0:
                    v[wy][wx] = 1
                    Q1.append([wy, wx])
                    Q2.append([wy, wx])
                    s[0] = wy
                    s[1] = wx
                else:
                    g += 1
            temp = R % len(Q1)
            for f in range(temp):
                a = Q1.pop()
                Q1 = [a] + Q1
            for f in range(len(Q1)):
                v[Q2[f][0]][Q2[f][1]] = l[Q1[f][0]][Q1[f][1]]
for i in v:
    print(*i)
