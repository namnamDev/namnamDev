import sys

sys.stdin = open("Baekjoon1189.txt")


def dfs(y, x, cnt):
    global an
    global visitied
    if visitied[end[0]][end[1]]:
        if cnt > K - 1:
            pass
        elif cnt == K - 1:
            an += 1
        return

    if visitied[end[0]][end[1]] and cnt == K - 1:
        print()
        for i in visitied:
            print(i)
        print(cnt)
        an += 1
        print("plus", an)
        return

    else:
        for i in range(4):
            wy = y + diry[i]
            wx = x + dirx[i]
            if 0 <= wy < R and 0 <= wx < C:
                if board[wy][wx] == "." and visitied[wy][wx] == 0:
                    visitied[wy][wx] = 1
                    dfs(wy, wx, cnt + 1)
                    visitied[wy][wx] = 0


diry = [-1, 1, -0, 0]
dirx = [0, 0, -1, 1]
R, C, K = map(int, input().split())
board = [list(input()) for _ in range(R)]
start = (R - 1, 0)
end = (0, C - 1)
an = 0
visitied = [[0] * C for _ in range(R)]
visitied[start[0]][start[1]] = 1
dfs(start[0], start[1], 0)
print(an)
