import sys

sys.stdin = open('0611test.txt')

# diry = [-1, 1, 0, 0]
# dirx = [0, 0, -1, 1]
# def goRoard():
#
H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# for i in board:
#     print(i)
dp = [[0] * H for _ in range(W)]
# vi = [[[] * 1] * H for _ in range(W)]
# vi[0][0] = [0, 0]
# dp[0] = [0] + board[0]
for i in range(1, H):
    dp[0][i] += dp[0][i - 1] + board[0][i]
    # vi[0][i].append([0, i])
for i in range(1, W):
    dp[i][0] += dp[i - 1][0] + board[i][0]
    # vi[i][0].append([i, 0])
# print(dp[0])
# an = [[0, 0]]
# for i in range(1, H):
#     for g in range(1, W):
# an.append()
# for i in vi:
#     print(i)
arr = []
for i in range(1, H):
    for g in range(1, W):
        if dp[i - 1][g] >= dp[i][g - 1]:
            arr.append([i, g - 1])
        else:
            arr.append([i - 1, g])
        dp[i][g] = board[i][g] + min(dp[i - 1][g], dp[i][g - 1])

for i in dp:
    print(i)
print(arr)
