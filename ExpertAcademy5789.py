import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5789.txt")

for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    li = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for g in range(L - 1, R):
            # print(g)
            li[g] = i
    print("#{}".format(tc), end=" ")
    print(*li)
