import sys
sys.stdin = open("ExpertAcademy4864.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = input(), input()
    an = 0
    print(N)
    print(M)
    for i in range(len(M)-len(N)+1):
        find = False
        for g in range(len(N)):
            print(M[i+g], N[g])
            if M[i+g] != N[g]:
                break
            if g == len(N)-1:
                an = 1
                find = True
        if find:
            break
    print("#{} {}".format(tc, an))