T = int(input())
board = []
for i in range(T):
    li = list(input())
    board+= [li]
ga = 0
se = 0
for i in board :
    cnt = 0
    for g in i:
        if g =='.':
            cnt+=1
        else :
            if cnt >= 2:
                ga+=1
            cnt = 0
    if cnt>=2:
        ga+=1

for i in range(T):
    cnt = 0
    for g in range(T):
        dot=board[g][i]
        if dot == '.':
            cnt+=1
        else :
            if cnt>=2:
                se +=1
            cnt =0
    if cnt >=2:
        se+=1

print(ga,se)