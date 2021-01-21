T = int(input())
def myF(a,b):
    ans = ''
    for i in range(int(b)):
        ans += a
    return ans

def myLen(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

for i in range(1,T+1):
    print(f'#{i}')
    N = int(input())
    answer = ''
    for g in range(N):
        nexs = input().split()
        answer += myF(nexs[0],nexs[1])
    
    lenlen = myLen(answer)
    cnt = 0
    while lenlen-10 >= 0 :
        if lenlen >= 0 :
            print(answer [-lenlen : -lenlen+10 ])
            lenlen -= 10
            cnt += 1
    print(answer[cnt*10 : ])

