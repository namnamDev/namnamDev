T = int(input())
def divdiv(a,b) :
    cnt =0
    while a%b ==0 :
        a = a//b
        cnt+=1
    return cnt

for i in range(1,T+1):
    num = int(input())
    answer =f'{divdiv(num,2)} {divdiv(num,3)} {divdiv(num,5)} {divdiv(num,7)} {divdiv(num,11)}'
    print(f'#{i} {answer}')