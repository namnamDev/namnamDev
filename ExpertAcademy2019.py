N = int(input())
answer = '1 '
intN = 1
for i in range(N):
    intN = intN*2
    answer += str(intN)+ ' ' 
print(answer)