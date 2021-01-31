N = input()

for i in N :
    f = ord(i)
    if(f >= 97) : 
        f -= 32

max = 0
answer = ''
for g in alpa_dic :
    if(max < alpa_dic.get(g)):
        max = alpa_dic.get(g)
print(alpa_dic)
