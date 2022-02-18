import sys
from pprint import pprint

sys.stdin = open("Baekjoon11286.txt")
N = int(input())
arrP = []
arrM = []
for tc in range(N):
    x = int(input())
    if x > 0:
        arrP.append(x)
    elif x < 0:
        arrM.append(x)
    else:
        arrP.sort(reverse=True)
        arrM.sort(reverse=True)
        print(arrP, arrM)
        if arrP and arrM:
            pM = abs(arrP[-1])
            Mm = abs(arrM[-1])
            if pM < Mm:
                print(arrP.pop())
            elif pM > Mm:
                print(arrM.pop())
            else:
                print(arrP.pop())
                arrM.pop()
        elif not arrP and arrM:
            print(arrM[-1])
            arrM.pop()
        elif not arrM and arrP:
            print(arrP[-1])
            arrP.pop()
        else:
            print(0)
