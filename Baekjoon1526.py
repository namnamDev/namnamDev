N = input()
T = 0
answer = []
N1=int(N[0])
if N1 < 4 :
    N.pop(0)
elif 4<=N1<7 :
    N[0] = '4'
else : 
    N[0] = '7'

for i in N :
    ii = int(i)
    temp = 0
    if 4 <= ii < 7 :
        temp = 4
    else :
        temp = 7
    answer+=[temp]

print(answer)