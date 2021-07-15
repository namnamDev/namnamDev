import sys

sys.stdin = open('Baekjoon1149.txt')
T = int(input())
board = [[0] * 3 for _ in range(T + 1)]
# vi = [[0] * 3 for _ in range(T + 1)]
for i in range(1, T + 1):
    x, y, z = map(int, input().split())
    # print(x, y, z)
    board[i][0] = min(board[i - 1][1], board[i - 1][2]) + x
    board[i][1] = min(board[i - 1][0], board[i - 1][2]) + y
    board[i][2] = min(board[i - 1][1], board[i - 1][0]) + z

print(min(board[T]))
