N = input()
an =''
res = {}
for i in N :
    f = ord(i)
    if(f >= 97) : 
        f -= 32
    an += chr(f)
ann = set(an)
maxs = 0 
for i in ann :
    temp = an.count(i)
    an = an.replace(i,'')
    res[temp] = res.get(temp,[]) + [i]
    if maxs < temp:
        maxs = temp

if len(res[maxs])>1:
    print('?')
else : print(*res[maxs])