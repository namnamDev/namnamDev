import sys

sys.stdin = open('Baekjoon14500.txt')


def copyArr():
    tempBoard = [[0] * M for _ in range(N)]
    for yt in range(N):
        for xt in range(M):
            tempBoard[yt][xt] = board[yt][xt]
    return tempBoard


def checkAdd(now, tet):
    paBoard = copyArr()
    cnt = 0
    for i in range(4):
        if not (0 <= now[0] + tet[i][0] < N and 0 <= now[1] + tet[i][1] < M):
            return 0
        else:
            cnt += paBoard[now[0] + tet[i][0]][now[1] + tet[i][1]]
    return cnt


tet1 = [[0, 1], [1, 1], [2, 1], [0, 1]]
tet2 = [[0, 0], [0, 1], [1, 0], [2, 0]]
tet3 = [[0, 0], [0, 1], [0, 2], [0, 3]]  # 회전2회
tet4 = [[0, 1], [1, 1], [1, 0], [2, 0]]  # 회전2회
tet5 = [[0, 0], [1, 0], [0, 1], [1, 1]]  # 회전 x
tets = [tet1, tet2, tet3, tet4, tet5]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

maxs = []
for y in range(N):
    for x in range(M):
        # for r in range(4):

        for tetIdx in range(5):
            tet = tets[tetIdx]
        # for tet in tets:
        #     cnt = checkAdd([y, x], tet)
        #     if cnt:
        #         print(cnt, y, x, tet)
        #         maxs.append(cnt)
print(maxs)
print(max(maxs))
