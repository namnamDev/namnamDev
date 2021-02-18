import sys
sys.stdin = open("ExpertAcademy5432.txt")
T = int(input())
for tc in range(1,T+1):
    bar = input()
    laser = "()"
    lenBar = len(bar)
    li = [0]*lenBar
    # for g in range(0,len(bar),2):
    #     if laser in bar:
    #         bar = bar.replace(laser, "--")
    #         li[g], li[g+1] = -1, -1
    leftCnt = 0
    i = 0
    while i < lenBar:
        if "(" == bar[i]:
            if ")" != bar[i+1]:
                leftCnt += 1
                li[i] = leftCnt
            else:
                li[i] = 0
                li[i+1] = 0
                i += 1
        elif ")" == bar[i]:
            li[i] = leftCnt
            leftCnt -= 1
        i += 1
    g = 0
    while g < lenBar:
        if 3 == li[g]:
            cnt = 0
            for gg in range(g+1, lenBar):
                if 3 == li[gg]:
                    cnt = gg
                    break
            temp = li[g:cnt+1]
            g = cnt + 1
            cnts = 0
            for f in temp:
                if [0,0] in temp:
                    cnt + 1
            print(a)
        else:
            g += 1
        # print(g)

    print(bar)
    print(li)
