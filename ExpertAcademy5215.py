import sys

sys.stdin = open("ExpertAcademy4613.txt")


def coloring(start, y):
    a = 0
    global minN
    if y == 3:
        if visited[N - 1] and visited == sorted(visited):
            for i in range(N):
                for g in range(M):
                    if arr[i][g] != color[visited[i]]:
                        a += 1
            if a < minN:
                minN = a
        return
    for i in range(start, N - (2 - y)):
        visited[i] = y
        coloring(i + 1, y + 1)


color = ["W", "B", "R"]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [0] * N
    cnt = 0
    minN = M * N
    coloring(0, 0)
    print("#{} {}".format(tc, minN))
