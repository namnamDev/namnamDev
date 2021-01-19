T = int(input())
listN = []
answer = []
line = input().split()
for i in line:
    intI = int(i)
    listN.append(intI)
listN.sort()


mid = int((T-1)/2)
print(listN[mid])


