import sys

sys.stdin = open('Baekjoon1236.txt')
N, M = map(int, input().split())
board = [[] for _ in range(N)]
viN = [0] * N
viM = [0] * M
for i in range(N):
    board[i] = list(input())
    for g in range(M):
        if board[i][g] == "X":
            viN[i] = 1
            viM[g] = 1
print(max(viN.count(0), viM.count(0)))
