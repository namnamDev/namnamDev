import sys

T = int(sys.stdin.readline())
cnt = 0
tu369 = (3,6,9)
while T >= 10:
    cnt+=1
    sums = 0
    temp = T
    while temp >= 10 :
        sums += temp%10
        temp = temp//10
        print(temp, sums)
    T = sums

print(cnt)
if T in tu369 :
    print('YES')
else : 
    print('NO')
