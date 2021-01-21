def snail(N):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    li = []
    for z in range(N):
        li.append([0]*N)
    d=0
    i=2
    x, y = 0, 0
    li[x][y] = 1

    while i <= N**2:
        if -1 < x+dx[d%4] < N and -1 < y+dy[d%4] < N and li[x+dx[d%4]][y+dy[d%4]] == 0:
            x += dx[d%4]
            y += dy[d%4]
            li[x][y] = i
            i += 1
        else:
            d += 1

    return li


T = int(input())
for k in range(T):
    mission = int(input())
    print('#{} '.format(k+1))
    for m in range(mission):
        result_li = snail(mission)
        print(*result_li[m]) 