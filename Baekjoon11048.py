import sys

sys.stdin = open('Baekjoon11048.txt')
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
vi = [[0] * M for _ in range(N)]
vi[0][0] = board[0][0]
for i in range(1, N):
    vi[i][0] = vi[i - 1][0] + board[i][0]
for g in range(1, M):
    vi[0][g] = vi[0][g - 1] + board[0][g]

for y in range(1, N):
    for x in range(1, M):
        vi[y][x] = board[y][x] + max(vi[y - 1][x], vi[y][x - 1])
print(vi[-1][-1])
