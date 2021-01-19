a = int(input())

for i in range(0,a) :
    sum = 0
    b = input().split()
    for a in b:
        intA = int(a)
        if intA%2!=0:
            sum = sum + intA
    print(f'#{i+1} {sum}')


