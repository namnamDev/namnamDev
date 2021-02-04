def solution(board, moves): #크래인 뽑기
    answer = 0
    li = []
    boards=len(board)
    for move in moves :
        move-=1
        for x in range(boards) :
            if board[x][move] :
                li += [board[x][move]]
                print(x,move,[board[x][move]])
                board[x][move] = 0
                break
                
        if len(li)>=2 :
            if li[-2]==li[-1]:
                answer+=2
                li.pop(-1)
                li.pop(-1)
    return answer