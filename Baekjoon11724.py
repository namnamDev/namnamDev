import sys

sys.stdin = open('Baekjoon11724.txt')
N, M = map(int, input().split())
board = [[0] * (N + 1) for _ in range(N + 1)]
vi = [0] * (N + 1)
for i in range(M):
    fir, sec = map(int, input().split())
    board[fir][sec] = 1
    board[sec][fir] = 1
aaa = []
for g in range(1, N + 1):
    if not vi[g]:
        vi[g] = 1
        S = [g]
        aa = [g]
        while S:
            temp = S.pop()
            print(temp)
            line = board[temp]
            for i in range(N + 1):
                if line[i] and not vi[i]:
                    vi[i] = 1
                    S.append(i)
                    aa.append(i)
        aaa.append(aa)
print(len(aaa))
