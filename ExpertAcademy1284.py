T =int(input()) #테스트케이스
for i in range(T) :
    line = input().split()
    for f in range(5):
        line[f] = int(line[f])
    P = line[0] #A사 리터당 요금
    Q = line[1] #B사 R리터 이하 요금
    R = line[2] #기준 리터
    S = line[3] #B사 R리터 이상 1L당 요금
    W = line[4] #종민이 한달 사용량
    sumA = P*W
    sumB = Q+ (W-R)*S if W>R else Q 
    answer = sumB if sumA > sumB else sumA

    print(f'#{i+1} {answer}')
