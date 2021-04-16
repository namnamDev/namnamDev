import sys

sys.stdin = open("ExpertAcademy2819.txt")


def powerset(num, idx):
    if len(num) == M:
        if dict.get(num, 1):
            dict[num] = 0
        return
    else:
        for i in range(4):
            wy = dry[i] + idx[0]
            wx = drx[i] + idx[1]
            if 0 <= wy < N and 0 <= wx < N:
                powerset(num + board[wy][wx], [wy, wx])


dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]

for tc in range(int(input())):
    N = 4
    M = 7
    board = [list(input().split()) for _ in range(N)]
    dict = {}
    for i in range(N):
        for g in range(N):
            powerset(board[i][g], [i, g])
    print("#{} {}".format(tc + 1, len(dict)))
