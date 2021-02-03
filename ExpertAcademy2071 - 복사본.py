T = int(input())
for i in range(0,T) : 
    lists =input().split()
    sumN = 0
    for num in lists :
        intN = int(num)
        sumN = sumN + intN
    avg = round(float(sumN/len(lists)))
    print(f'#{i+1} {avg}')

