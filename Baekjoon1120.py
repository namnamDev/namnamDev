A, B = input().split()
lenA = len(A)
lenB = len(B)
minCnt = 50
minIdx = 0
for i in range(lenB - lenA + 1):
    temp = 0
    tempIdx = 0
    for g in range(lenA):
        if A[i] != B[g]:
            temp += 1
    if minCnt > temp:
        minCnt = temp
        minIdx = i
print(minCnt, minIdx)
