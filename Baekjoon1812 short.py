T = int(input())
s,c,z = [],[],0
for f in range(T) :
    h = int(input())
    s += [h]
    z += -h if f%2 else h
c+=[z//2]
for i in range(0,T-1):
    c+= [s[i]-c[i]]
for i in c :
    print(i)
