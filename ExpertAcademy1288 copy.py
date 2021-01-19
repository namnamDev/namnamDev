T =int(input()) #테스트케이스
temp = {'',''}
def lenDics(temp):
    lenNum = 0
    for dd in asd:
        lenNum+=1
    return lenNum

for i in range(1,T+1):
    N = input()
    dics = {}
    cnt = 0
    lenDics = 0
    while lenDics(dics) != 10:
        cnt+=1
        for g in str(int(N)*cnt):
            dics[int(g)] = 1
    answer = str(int(N)*cnt)
    print(f'#{i} {answer}')
