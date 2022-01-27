import sys

sys.stdin = open("Baekjoon1051.txt")
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

maxSize = 0

for y in range(N - maxSize):
    for x in range(M - maxSize):
        s = 0
        while 0 <= y + s < N and 0 <= x + s < M:
            if board[y][x] == board[y + s][x] == board[y][x + s] == board[y + s][x + s]:
                maxSize = max(s + 1, maxSize)
            s += 1
print(maxSize ** 2)
