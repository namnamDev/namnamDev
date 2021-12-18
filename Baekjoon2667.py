import sys

sys.stdin = open('Baekjoon2210.txt')


def dfs(paArr, ny, nx):
    if len(paArr) == 6:
        if paArr not in answer:
            answer.append(paArr)
        return
    for dirs in range(4):
        wy = ny + diry[dirs]
        wx = nx + dirx[dirs]
        if 0 <= wy < 5 and 0 <= wx < 5:
            dfs(paArr + [board[wy][wx]], wy, wx)


board = [list(map(int, input().split())) for _ in range(5)]
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
answer = []

for yy in range(5):
    for xx in range(5):
        dfs([], yy, xx)
print(len(answer))
