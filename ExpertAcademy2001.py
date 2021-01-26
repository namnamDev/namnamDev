T  = int(input())
def kill_fly(starts,ends,boards):
    kill = 0 
    for i in range(starts,ends) :
        for g in range(starts,ends):
            kill +=boards[i][g]
    return kill
    
#     print(boardN)
for i in range(1,T+1):
    line = list(map(int, input().split()))
    M , N= line[0] , line[1]
    boards = []
    for lines in range(M):
        ss = list(map(int,input().split()))
        boards.append(ss)
    max_kill = 0

    for kills in range(M-N+1):
        for g in range(M-N+1):
            temp = kill_fly(kills,g,boards)
            print(kills , g ,temp)
            if max_kill < temp :
                max_kill = temp
    print(f'#{i} {max_kill}')
    # print(boards)
# kill_fly(5,4,'b')