import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1227.txt")

SIZE = 100

for _ in range(1, 11):
    tc = int(input())
    li = [0] * SIZE
    for g in range(SIZE):
        li[g] = list(map(int, input()))
    # print(tc)
    # pprint(li)
    start = 0
    end = 0
    for i in range(SIZE):
        for ii in range(SIZE):
            if li[i][ii] == 2:
                start = [i, ii]
            elif li[i][ii] == 3:
                end = [i, ii]
            if start and end:
                break
        if start and end:
            break

    # print(start, end)

    drx = [1, -1, 0, 0]
    dry = [0, 0, 1, -1]
    now = start
    stack = []
    an = 0
    for x in range(SIZE):
        for y in range(SIZE):
            for dir in range(4):
                willx = now[0] + drx[dir]
                willy = now[1] + dry[dir]
                if li[willx][willy] != 1:
                    stack += [[willx, willy]]
            if len(stack) > 0:
                now = stack.pop()
                # print(now, li[now[0]][now[1]])
                if li[now[0]][now[1]] == 3:
                    an = 1
                    break
                else:
                    li[now[0]][now[1]] = 1
            else:
                break
    print("#{} {}".format(tc, an))
