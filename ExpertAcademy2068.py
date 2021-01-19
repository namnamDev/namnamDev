T = int(input())
for i in range(T) :
    temp = 0
    b = input().split()
    maxs = 0
    tempA = []
    for a in b:
        intA = int(a)
        tempA.append(intA)
    for a in tempA :
        if maxs < a:
            maxs = a
    print(f'#{i+1} {maxs}')