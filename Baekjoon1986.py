import sys

sys.stdin = open("Baekjoon1986.txt")

kndiry = [-1, -1, -2, -2, 1, 1, 2, 2]
kndirx = [-2, 2, -1, 1, -2, 2, -1, 1]
Qdiry = [-1, -1, 0, 0, 1, 1, -1, 1]
Qdirx = [0, -1, 1, -1, 0, 1, 1, -1]
N, M = map(int, input().split())
board = [[0] * N for _ in range(M)]
for i in range(3):
    arr = list(map(int, input().split()))
    cnt = arr.pop(0)
    for g in range(0, cnt * 2, 2):
        board[arr[g + 1] - 1][arr[g] - 1] = i + 1

for y in range(M):
    for x in range(N):
        if board[y][x] == 1:
            for i in range(8):
                wy = y + Qdiry[i]
                wx = x + Qdirx[i]
                while 0 <= wy < M and 0 <= wx < N:
                    if board[wy][wx] == 0 or board[wy][wx] == 7:
                        board[wy][wx] = 7
                        wy += Qdiry[i]
                        wx += Qdirx[i]
                    else:
                        break

        elif board[y][x] == 2:
            for i in range(8):
                wy = y + kndiry[i]
                wx = x + kndirx[i]
                if 0 <= wy < M and 0 <= wx < N:
                    if board[wy][wx] == 0 or board[wy][wx] == 7:
                        board[wy][wx] = 7
cnt = 0
for i in board:
    for g in i:
        if g == 0:
            cnt += 1
print(cnt)

for i in board:
    print(*i)
