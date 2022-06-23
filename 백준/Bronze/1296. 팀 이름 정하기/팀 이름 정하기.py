A = input()
arr = ["L", "O", "V", "E"]
nameCnt = [0] * 4
for idx in range(4):
    nameCnt[idx] = A.count(arr[idx])
N = int(input())
arra = {}
tmax = 0
for _ in range(N):
    teamName = input()
    temp = [0] * 4
    for idx in range(4):
        temp[idx] = nameCnt[idx] + teamName.count(arr[idx])
    total = 1
    for fidx in range(4):
        for sidx in range(fidx + 1, 4):
            total *= temp[fidx] + temp[sidx]
    tt = total % 100
    tmax = max(tmax, tt)
    if arra.get(tt):
        arra[tt].append(teamName)
    else:
        arra[tt] = [teamName]
aa = sorted(arra[tmax])
print(aa[0])