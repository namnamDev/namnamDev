import sys
sys.stdin = open("ExpertAcademy4865.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = input(), input()
    maxNum = 0
    for n in N:
        temp = 0
        for m in M:
            if n == m:
                temp += 1
                M = M.replace(n, "")
        if temp > maxNum:
            maxNum = temp

    print("#{} {}".format(tc, maxNum))