N = input()
alpalist = [0]*26
alpa_dic = {}
for i in N :
    f = ord(i)
    if(f >= 97) : 
        f -= 32
    if f not in alpa_dic:
        alpa_dic[f] = 1
    else :
        alpa_dic[f] += 1
max = 0
answer = ''
for g in alpa_dic :
    if(max < alpa_dic.get(g)):
        max = alpa_dic.get(g)
print(alpa_dic)
