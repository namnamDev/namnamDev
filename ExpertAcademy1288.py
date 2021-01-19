T =int(input()) #테스트케이스
for i in range(1,T+1):
    N = input()
    dics = {}
    cnt = 0
    lenDics = 0
    for lenDicsN in dics :
        lenDics+=1
    while len(dics) != 10:
        cnt+=1
        for g in str(int(N)*cnt):
            dics[int(g)] = 1
    answer = str(int(N)*cnt)
    print(f'#{i} {answer}')
