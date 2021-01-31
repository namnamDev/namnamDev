a = list(map(int,input().split()))
b = list(map(int,input().split()))
NM =  a[0]*a[1]
li = []
for i in b :
    i -= NM
    li+=[i]
print(*li)