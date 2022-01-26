import sys

sys.stdin = open('Baekjoon2609.txt')
N, M = map(int, input().split())
if N > M:
    N, M = M, N
arrN = [0] * (N + 1)
arrM = [0] * (M + 1)
tempN = N
tempM = M
while N > 1:
    for i in range(2, N + 1):
        if not N % i:
            N //= i
            arrN[i] += 1
            break
while M > 1:
    for i in range(2, M + 1):
        if not M % i:
            M //= i
            arrM[i] += 1
            break
minN1 = 1
maxN1 = 1
for i in range(tempN + 1):
    temp = min(arrN[i], arrM[i])
    temp2 = max(arrN[i], arrM[i])
    if temp:
        minN1 *= i ** temp
    if temp2:
        maxN1 *= i ** temp2
for ii in range(tempN + 1, tempM + 1):
    if arrM[ii]:
        maxN1 *= ii ** arrM[ii]

print(minN1)
print(maxN1)
# 2**3 3
# 2**1 3**2
