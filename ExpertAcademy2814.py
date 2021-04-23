import sys
from pprint import pprint
from pprint import pprint

sys.stdin = open("ExpertAcademy2814.txt")


def do_dfs(idx, arr):
    global max_cnt
    max_cnt = max(max_cnt, len(arr))
    for i in range(N):
        if board[idx][i] and not vi[i]:
            vi[i] = 1
            do_dfs(i, arr + [i])
            vi[i] = 0


for tc in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    for i in range(M):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        board[y][x] += 1
        board[x][y] += 1
    max_cnt = 0
    for i in range(N):
        vi = [0] * N
        vi[i] = 1
        do_dfs(i, [i])

    print("#{} {}".format(tc + 1, max_cnt))
