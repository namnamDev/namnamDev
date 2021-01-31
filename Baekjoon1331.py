move_list=[]
for i in range(36):
    move_list += [input()]

a = 0
for i in  range(1,36):
    now = move_list[i]
    fir = move_list[i-1]
    ords = abs(ord(now[0]) - ord(fir[0]))
    nums = abs(int(now[1]) -int(fir[1]))
    if ((ords == 1 and nums ==2) or (ords == 2 and nums ==1)) and move_list.count(now) == 1 :
        if 65<=ord(now[0])<=70 and 65<=ord(fir[0])<=70 and 1<=int(now[1])<=8 and 1<=int(fir[1])<=8:
            a=1
        else :
            a =0
            break
    else : 
        a=0
        break
if a :
    print('Valid')
else :
    print('Invalid')
