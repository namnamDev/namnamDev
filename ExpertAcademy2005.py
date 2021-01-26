answer = []
T = int(input())
for i in range(T):
    case_result = [1,[1,1]]
    N = int(input())
    temp = ''
    #00 
    #10 /11
    #20 21 22 #g=2 line0 1 2  2/1
    #30 31 32 33 g=3
    for g in range(2,N):
        temp_1= []
        for line in range(g+1):
            ones = 0
            # print('---')
            # print (g, line)
            # print('---')
            if line ==0 or line == g:
                ones = 1
            else :
                # print(g-1,line-1,g-1,line)
                sik = case_result[g-1][line-1]+case_result[g-1][line]
                ones = sik
            temp_1.append(ones)
        case_result.append(temp_1)
        # print(case_result)
    print(case_result)