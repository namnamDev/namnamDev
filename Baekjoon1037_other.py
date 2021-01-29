N = int(input())
yakList = list(map(int,input().split()))
yakList.sort(reverse=True)
answer = 0
for i in range(yakList[0]+1,2**16) :
    for g in yakList:
        if i%g != 0 :
            answer= 0
            break
        else :
            answer = i
    if answer !=0:
        break
print(answer)
