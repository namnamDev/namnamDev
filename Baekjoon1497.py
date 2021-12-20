import sys

sys.stdin = open('Baekjoon1497.txt')


def com(paArr, idx):
    if len(paArr) == ll:
        print(paArr)
        vi = [0] * M
        for ii in paArr:
            ak = songs[ii]
            for ii in range(M):
                if not vi[ii] and ak[ii] == "Y":
                    vi[ii] = 1
        cntSongs = vi.count(1)
        board[ll] = max(board[ll], cntSongs)
        return
    for i in range(idx, N):
        com(paArr + [i], i + 1)


N, M = map(int, input().split())
songs = []
for i in range(N):
    a, b = input().split()
    songs.append(list(b))
an = 0
board = [0] * (N + 1)
for i in range(1, N + 1):
    ll = i
    com([], 0)
    an = max(an, board[ll])
    if an == M:
        break
ann = 0
for rr in range(N + 1):
    if board[rr] == an:
        ann = rr
        break
if not an:
    ann = -1
print(ann)
