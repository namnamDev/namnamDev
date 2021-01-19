t = int(input())
sums = 0
cnts = 0
lists = []
for i in range(t) :
    lists.append((input()))
years = ''
months = ''
dates = ''
day31 = list(range(1,31))
day30 = list(range(1,30))
day28 = list(range(1,28))
tables = [day31,day28, day31, day30, day31, day30, day31,day31,day30,day31,day30,day31] 
answer = '-1'
for i in lists :
    lens = 1
    cnts += 1
    years = i[0:4]
    months = i[4:6]
    dates = i[6:8]
    if int(months)>12 or int(months) <1  :
        # print('1번 에러')
        answer ='-1'
    else:
        for  i in tables[int(months)-1]:
            lens += 1
            intDate = int(dates)
        # print(lens)
        if lens < intDate or intDate <1 :
            answer = '-1'
            # print('2번에러')
        else: answer = f'{years}/{months}/{dates}'
    print(f'#{cnts} {answer}')




