T = int(input())
for i in range(1,T+1) :
    S =input().split()
    hours = [int(S[0]),int(S[2])]
    minutes =[int(S[1]),int(S[3])]
    result_min = minutes[0]+minutes[1]
    cnt = 0
    if result_min>=60 :
        result_min -=60
        cnt += 1
    result_hour = (hours[0]+hours[1]+cnt)%12
    if result_hour == 0 :
        result_hour = 12
    print(f'#{i} {result_hour} {result_min}')