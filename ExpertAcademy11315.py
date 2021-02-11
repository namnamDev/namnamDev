# import sys
# sys.stdin = open("ExpertAcademy11315.txt")

def my_row(arr,N):
    result = False
    for i in range(N-5,N):
        for g in range(N-5,N):
            # if arr[i][g] == 'o':
            print(i,g)
            rows = arr[i][g:g+5]
            cols = arr[g:g+5][i]
            digs = arr[g:g+5][i:i+5]
            print(rows, cols, digs)


    return result

T = int(input())
N = int(input())
board = []
for i in range(N):
    board += [list(input())]
my_row(board, N)

# print(board)