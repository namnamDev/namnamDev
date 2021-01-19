T = int(input())
def myF(a,b):
    ans = ''
    for i in range(int(b)):
        ans += a
    return ans

for i in range(1,T+1):
    TT = int(input())
    answer = ''
    for g in range(TT):
        nexs = input().split()
        answer += myF(nexs[0],nexs[1])
    
    
    tenten = 0
    anan = ''
    page = 0
    sstring = ''
    cnt = 0

    for f in answer:
        cnt+=1
    print(f'#{i}')
    while cnt > 0:
        if cnt>=10:
            page += 1
            for ff in range(page*10-9,page*10) :
                sstring += answer[ff]
        else :
            for ff in range(page*10, page*10 + cnt%10) :
                sstring += answer[ff]
        print(sstring)
        sstring = ''
        cnt -= 10 

