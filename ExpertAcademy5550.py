import sys
from pprint import pprint
sys.stdin = open("ExpertAcademy5356.txt")
T = int(input())
for tc in range(1, T+1):
    N = 5
    li = [0]*N
    maxLen = 0
    for i in range(N):
        li[i] = list(input())
        if maxLen < len(li[i]):
            maxLen = len(li[i])
    # pprint(li)
    an = ""
    for g in range(maxLen):
        for f in range(N):
            if g < len(li[f]):
                an += li[f][g]
                # print(an)

    print("#{} {}".format(tc, an))