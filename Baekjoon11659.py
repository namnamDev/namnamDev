import sys

sys.stdin = open("Baekjoon11659.txt")
input = sys.stdin.readline
a, b = map(int, input().split())
arr = list(map(int, input().split()))
board = [0] * (a + 1)
board[1] = arr[0]
for i in range(2, a + 1):
    board[i] = board[i - 1] + arr[i - 1]
print(board)
for t in range(b):
    f, e = map(int, input().split())
    print(board[e] - board[f - 1])
# board = [[0] * a for _ in range(a)]
# board[0][0] = arr[0]
# for i in range(1, a):
#     board[0][i] = board[0][i - 1] + arr[i]
#     print(board[0][i])
# for fir in range(1, a):
#     for end in range(fir + 1, a):
#         board[fir][end] = board[fir][end - 1] -
# print(board[0])
# 5 4 3 2 1
# 0  1  2  3  4  5
# 1  5  9 12 14 15
# 2     4  7
# 3
# 4
# 5
