T = int(input())
for f in range(T):
    PV = input().split()
    P = int(PV[0])
    V = int(PV[1])
    arrays = []
    for i in range(P):
        lines = input().split()
        arrays.append(lines)
    print(f'#{f+1}')
    for i in range(P):
        line = arrays[i]
        cnt = 0
        dots = []
        for g in range(V):
            if line[g] == '1' :
                cnt+=1
                dots.append([i,g])
            
        if cnt == 2 :
            ff = dots[0][0]
            fs = dots[0][1]
            sf = dots[1][0]
            ss = dots[1][1]
            print(f'좌표:({ff},{fs}),({sf},{ss}), 길이:{dots[1][1]-dots[0][1]+1}')
