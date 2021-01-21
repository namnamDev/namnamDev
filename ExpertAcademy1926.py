T = int(input())
answer = ''
def myF(a):
    
for i in range(1,T+1) :
    temp =''
    cnt = 0
    for g in str(i):
        if g in ['3','6','9'] :
            cnt += 1
    if(cnt!=0) :
        for i in range(cnt):
            temp += '-'
    else :
        temp += str(i) 
    answer += temp+ ' '

print(answer)
