T = int(input())
for case in range(1,T+1):
    N = int(input())
    boards = []
    result = []
    for i in range(N):
        lines = list(map(int , input().split()))
        boards.append(lines)

    for line in range(N):
        temp_fir = ''
        temp_sec = ''
        temp_thir = ''
        for g in range(N):
            temp_fir += str(boards[N-g-1][line])
            temp_sec += str(boards[N-1-line][N-g-1])
            temp_thir += str(boards[g][N-1-line])
        temp = temp_fir + ' ' + temp_sec + ' '+temp_thir
        result.append(temp)
    sec_boards = []
    
    print(f'#{case}')
    for i in result :
        print(i)