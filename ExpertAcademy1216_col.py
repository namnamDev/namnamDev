import sys

sys.stdin = open("ExpertAcademy1216.txt")
N = 100
for tc in range(1, 11):
    T = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(input())
    maxCnt = 0
    gase = ""
    for c in range(N):
        for f in range(N-1):
            temp = [arr[c][f], arr[c][f + 1]]
            # print(temp)
            tempF = f+1
            cnt = 0
            while tempF < N-1:
                for g in range(len(temp) // 2):
                    if temp[g] != temp[-g - 1]:
                        if tempF < N-1:
                            tempF += 1
                            temp += [arr[c][tempF]]
                            # print(temp)
                        break

                    if g == len(temp) // 2-1:
                        if maxCnt < len(temp):
                            maxCnt = len(temp)
                            gase = "ga"
                        if tempF < N-1:
                            tempF += 1
                            temp += [arr[c][tempF]]
                            # print(temp)
                # print(temp)
    # print("-------"+str(tc)+"-----")
    for cc in range(N):
        for ff in range(N-1):
            temp = [arr[ff][cc], arr[ff+1][cc]]
            # print(temp)
            tempC = ff+1
            cnt = 0
            while tempC < N-1:
                for g in range(len(temp) // 2):
                    if temp[g] != temp[-g - 1]:
                        if tempC < N-1:
                            tempC += 1
                            temp += [arr[tempC][cc]]
                            # print(temp)
                        break

                    if g == len(temp) // 2-1:
                        if maxCnt < len(temp):
                            maxCnt = len(temp)
                            gase = "se"
                        if tempC < N-1:
                            tempC += 1
                            temp += [arr[tempC][cc]]
                            # print(temp)
                # print(temp)
    print("#{} {}".format(T, maxCnt))
