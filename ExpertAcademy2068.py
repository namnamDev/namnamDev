T = int(input())
for i in range(0,T) :
    sum = 0
    b = input().split()
    max = 0
    tempA = []
    tempB = []
    for a in b:
        intA = int(a)
        tempA.append(intA)
    print(tempA)
    tempB = list(set(tempA))
    print(tempB)
    max = tempB[len(tempB)-1]
    print(f'#{i+1} {max}')

