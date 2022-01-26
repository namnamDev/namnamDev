import sys

sys.stdin = open("Baekjoon2563.txt")
N = int(input())
s = 100
board = [[0] * s for _ in range(s)]
for i in range(N):
    x, y = map(int, input().split())
    for yy in range(10):
        for xx in range(10):
            board[y + yy][x + xx] = 1
an = 0
for a in range(s):
    for b in range(s):
        if board[a][b]:
            an += 1
print(an)
