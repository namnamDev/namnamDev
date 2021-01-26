T = int(input())
def check(a):
    aa = set(a)
    if(len(aa))!=9:
        return 0
    else :
        return 1

for case in range(1,T+1) :
    oneBoard = []
    for i in range(9):
        line = list(map(int,input().split()))
        oneBoard.append(line)
    result = 0
    # print(oneBoard)
    for i in oneBoard:
        answer_1 = check(i)
        print(answer_1)


    # print('----')
    col = []    
    for i in range(9) :
        temp = []
        for g in range(9):
            temp.append(oneBoard[g][i])
        col.append(temp)

    for i in oneBoard :
        answer_2 =check(i)
        print(answer_2)

    # print(col)
    binggo = []
    for f in range(0,9,3):
        for h in range(0,9,3):
            temp_2 = []
            for i in range(3):
                for g in range(3):
                    temp_2.append(oneBoard[i+f][g+h])
            binggo.append(temp_2)
    for i in binggo:
        answer_3 =check(i)
        print(answer_3)

    if answer_1 and answer_2 and answer_3 == 1 :
        result = 1
    else :
        result = 0

    print(f'#{case} {result}')
    # for i in range(0,4,3):# 1,2,3
    #     for f in range(3):
    #         for g in range(3):
    #             binggo.append(oneBoard[i+f][g])
    #             print(binggo)
    

