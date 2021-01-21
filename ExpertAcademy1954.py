T = int(input())
for i in range(T) :
    N = int(input())
    board = [[0 for i in range(N)] for j in range(N)]
    # print(board)
    num = 1
    cnt = 0
# board 좌표
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# board 좌표
# 00 01 02 
# 10 11 12 
# 20 21 22 
    for i in range(N,N//2+1,-1):
        print('-----' + str(i)+ '-----')
        for g in range(i): # board[1]의 값들 알아서 출력
            board[N-i][g] = num
            print(f'N-i = {N-i} ; g = {g} ; {num} ; {board[N-i][g]} ')
            num+=1
        for f in range(N-i+1,i):
            board[f][i-1] = num
            print(f'f = {f} ; i-1 = {i-1} ; {num} ; {board[f][i-1]} ')
            num+=1
        for h in range(i-1,N-i,-1):
            board[i-1][h-1] = num
            print(f'i-1 = {i-1} ; h-1 = {h-1} ; {num} ; {board[i-1][h-1]} ')
            num+=1
        for k in range(i,N-i+1,-1):
            board[k-1][N-i] = num
            print(f'k-1 = {k-1} ; N-i = {N-i} ; {num} ; {board[k-1][N-i]} ')
            #board[3][0]
            num+=1

    for i in board :
        print(*i)

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33