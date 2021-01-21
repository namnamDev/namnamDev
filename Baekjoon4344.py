C = int(input())

for i in range(C):
    line = input().split()
    num = int(line[0])
    sums = 0
    cnt = 0
    for g in range(1,num) :
        sums += int(line[g])
        cnt += 1
    avg = sums/cnt

    cnt = 0
    for g in range(1,num) :
        if int(line[g]) > avg :
            cnt+=1

    answer = cnt/num
    ban = int(answer*1000000)
    banban = ban%10
    if banban >= 5:
        ban = ban+10 - banban
    else:
        ban = ban - banban
    answer = ban/10000
    # print(ban)

    print(answer)
    


