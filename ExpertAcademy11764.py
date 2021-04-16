import sys

sys.stdin = open('ExpertAcademy11764.txt')
for tc in range(int(input())):
    Ns, Ms = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))
    arrN.sort(reverse=True)
    arrM.sort(reverse=True)
    an = 0
    g = -1
    print(arrM)
    print(arrN)
    for i in range(Ms):
        while g < Ns - 1:
            g += 1
            if arrM[i] >= arrN[g]:
                an += arrN[g]
                print(arrN[g], end=' ')
                break
        if g == Ns - 1:
            break
    print()
    print("#{} {}".format(tc + 1, an))
    # for g in range(i, Ns):
    #     if arrM[i] >= arrN[g]:
    #         an += arrN[g]
    #         break
