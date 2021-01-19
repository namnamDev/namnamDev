T = int(input())
for f in range(1,T+1) :
    x = int(input())
    lists = input().split()
    lists.append('0')
    lists = [int (i) for i in lists]
    sample = []
    print(lists)
    max = 0
    maxwh = 0
    start = 0
    for i in range(x):
        if max < lists[i]:
            max = lists[i]
            maxwh = i+1
            start = i
    print(f'이게답인가 {lists[start : maxwh]}')
    sample.append(lists[start : maxwh])
        
    
    print(f'#{f}')
