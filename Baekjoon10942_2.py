import sys

sys.stdin = open('Baekjoon10942.txt')
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
quest = [list(map(int, input().split())) for _ in range(M)]
board = [[-1] * N for _ in range(N)]
# for i in range(N):
#     for g in range(i + 1, N + 1):
for size in range(1, N + 1):
    i = 0
    while i < N:
        temp_i = i
        g = i + size
        temp_g = g
        print(temp_i, temp_g, arr[temp_i:temp_g])
        while temp_i < temp_g <= N:
            if board[temp_i][temp_g - 1] != -1:
                print('he', board[temp_i][temp_g - 1])
                board[i][g - 1] = board[temp_i][temp_g - 1]
                break
            else:
                temp = arr[temp_i:temp_g]
                if temp[0] == temp[len(temp) - 1]:
                    temp_i += 1
                    temp_g -= 1
                else:
                    board[i][g - 1] = 0
                    break
                if temp_i >= temp_g:
                    board[i][g - 1] = 1
        i += 1
    for f in board:
        print(f)
for i in quest:
    print(board[i[0] - 1][i[1] - 1])
