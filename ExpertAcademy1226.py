import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy1226.txt")

for _ in range(1, 11):
    tc = int(input())
    li = [0] * 16
    for g in range(16):
        li[g] = list(map(int, input()))
    # print(tc)
    # pprint(li)
    start = 0
    end = 0
    for i in range(16):
        for ii in range(16):
            if li[i][ii] == 2:
                start = [i, ii]
            elif li[i][ii] == 3:
                end = [i, ii]
    # print(start, end)

    drx = [1, -1, 0, 0]
    dry = [0, 0, 1, -1]
    now = start
    stack = []
    an = 0
    for x in range(16):
        for y in range(16):
            for dir in range(4):
                willx = now[0] + drx[dir]
                willy = now[1] + dry[dir]
                if li[willx][willy] != 1:
                    stack += [[willx, willy]]
            if len(stack) > 0:
                now = stack.pop()
                print(now, li[now[0]][now[1]])
                if li[now[0]][now[1]] == 3:
                    an = 1
                    break
                else:
                    li[now[0]][now[1]] = 1
            else:
                break
    print("#{} {}".format(tc, an))
