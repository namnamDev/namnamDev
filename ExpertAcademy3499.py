import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy3499.txt")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    i = 0
    an = 1 if N % 2 else 0
    temp1 = card[:N // 2 + an]
    temp2 = card[N // 2 + an:]
    # print(temp1, temp2)
    temp3 = []
    for g in range(N // 2):
        temp3 += [temp1[g], temp2[g]]
    if an:
        temp3 += [temp1[-1]]
    card = temp3
    i += 1
    print("#{}".format(tc), end=" ")
    print(*card)
