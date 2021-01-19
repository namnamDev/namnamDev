T = int(input())
for i in range(1,T+1) :
    lists = input().split()
    aa = int(lists[0])
    bb = int(lists[1])
    cc = ''
    if aa < bb :
        cc = '<'
    if aa == bb : 
        cc = '='
    if aa > bb :
        cc = '>'
    print(f'#{i} {cc}')