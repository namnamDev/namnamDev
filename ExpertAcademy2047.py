N = input()
big = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
mini = list('abcdefghijklmnopqrstuvwxyz')
answer = ''
temp = ''
for i in N :
    for g in range(26):
        if mini[g] == i:
            temp= big[g]
            break
        else :
            temp=i
    answer += temp
print(answer)