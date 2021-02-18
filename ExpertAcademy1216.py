import sys

sys.stdin = open("ExpertAcademy1216.txt")
T = int(input())
N = 100
for tc in range(1, T + 1):
    arr = [0] * N
    for i in range(N):
        arr[i] = list(input())
    maxCnt = 0
    for c in range(N):
        for f in range(N-1):
            temp = [arr[c][f], arr[c][f + 1]]
            # print(temp)
            tempF = f+1
            cnt = 0
            while tempF < N:
                for g in range(len(temp) // 2):
                    if temp[g] != temp[-g - 1]:
                        if tempF < N:
                            temp += [arr[c][tempF]]
                            # print(temp)
                            tempF += 1
                        break

                    if g == len(temp) // 2-1:
                        if maxCnt < len(temp):
                            maxCnt = len(temp)
                        if tempF < N:
                            temp += [arr[c][tempF]]
                            # print(temp)
                            tempF += 1
                # print(temp)
    print(maxCnt -1)