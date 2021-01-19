N = input()
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
answer = ''
for i in N :
    for g in range(26):
        if a[g] == i:
            answer += str(g+1) + ' '
print(answer)