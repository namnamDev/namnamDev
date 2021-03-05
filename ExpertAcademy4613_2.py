import sys

sys.stdin = open("ExpertAcademy4613.txt")


def coloring(start, y, cnt):
    a = 0
    if y == 3:
        if visited[N - 1]:
            print(visited, cnt)
        return
    for i in range(start, N - (2 - y)):
        # print(start, N - (2 - y), i)
        visited[i] = y
        for g in range(M):
            if arr[i][g] != color[y]:
                a += 1
        coloring(i + 1, y + 1, cnt + a)

    # for i in range(N):
    #     for g in range(M):
    #         if board


color = ["W", "B", "R"]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [0] * N
    cnt = 0
    coloring(0, 0, 0)
    print(arr)
    # meW = []
    # meB = []
    # meR = []
