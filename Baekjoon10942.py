import sys

sys.stdin = open('Baekjoon10942.txt')
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
quest = [list(map(int, input().split())) for _ in range(M)]
board = [[-1] * N for _ in range(N)]
for i in range(N):
    for g in range(i + 1, N + 1):
        temp_i = i
        temp_g = g
        while temp_i < temp_g:
            # if board[i][g-1] ==-1:
            temp = arr[temp_i:temp_g]
            if temp[0] == temp[len(temp) - 1]:
                temp_i += 1
                temp_g -= 1
            else:
                board[i][g - 1] = 0
                break
            if temp_i >= temp_g:
                board[i][g - 1] = 1

        print(i, g, temp)
print(N)
print(arr)
print(M)
print(quest)
for i in board:
    print(i)
for i in quest:
    print(board[i[0] - 1][i[1] - 1])
