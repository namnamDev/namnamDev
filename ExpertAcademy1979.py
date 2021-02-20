import sys
from pprint import pprint
sys.stdin=open("ExpertAcademy1979.txt")

def myDef(arr):
    an = 0
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[y][x]:
                cnt += 1
                # print(y, x, cnt)
            else:
                if cnt == M:
                    an += 1
                cnt = 0

            if x == N-1 and cnt == M:
                an += 1
    return an

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [0]*N
    for i in range(N):
        li[i] = list(map(int, input().split()))
    # pprint(li)
    answer = myDef(li)
    for g in range(N):
        for gg in range(g):
            li[g][gg], li[gg][g] = li[gg][g], li[g][gg]
    # pprint(li)
    answer2 = myDef(li)
    # print(answer2)
    print("#{} {}".format(tc, answer+answer2)) #가로만 먼저
