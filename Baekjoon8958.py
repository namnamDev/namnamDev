T = int(input())
for i in range(T):
    line = input()
    cnt = 1
    sums = 0
    for i in line:
        if i =='O':
            sums += cnt
            cnt+=1
        else :
            cnt = 1
    print(sums)