T = int(input())
lists = []
for i in range(T):
    lists.append(list(input().split()))
cnts = 0
for i in lists :
    cnts += 1
    i0 = int(i[0])
    i1 = int(i[1])
    mok = i0//i1
    na = i0%i1
    print(f'#{cnts} {mok} {na}')
