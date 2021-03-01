import sys

sys.stdin = open("ExpertAcademy1974.txt")


def check(li):
    if 0 in li:
        return 0
    else:
        return 1


def colCheck(N):
    visited = [0] * 9
    for lines in range(9):
        visited[li[N][lines] - 1] = 1
    return check(visited)


def rowCheck(N):
    visited = [0] * 9
    for lines in range(9):
        visited[li[lines][N] - 1] = 1
    return check(visited)


def boxCheck(N, M):
    visited = [0] * 9
    for n in range(N, N + 3):
        for lines in range(M, M + 3):
            visited[li[n][lines] - 1] = 1
    return check(visited)


for tc in range(1, int(input()) + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    an = 0
    an1 = 0
    an2 = 0
    for i in range(9):
        an = colCheck(i)
        if an == 0: break

        an1 = rowCheck(i)
        if an1 == 0: break
    for i in range(0, 9, 3):
        for g in range(0, 9, 3):
            an2 = boxCheck(i, g)
            if an2 == 0: break
        if an2 == 0: break
    print("#{} {}".format(tc, an & an1 & an2))
