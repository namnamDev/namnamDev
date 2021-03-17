import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5550.txt")

li = ["c", "r", "o", "a", "k"]
for tc in range(int(input())):
    st = input()
    used = [0] * len(st)
    g = 0
    cnt = 0
    ms = 0

    while g < len(st) - 4:
        i = g
        temp = 0
        if st[g] == "c":
            mt = 0
            while i < len(st):
                if st[i] == li[temp] and used[i] == 0:
                    used[i] = 1
                    temp += 1
                i += 1

                if temp == 5:
                    temp = 0
                    cnt += 1
                    mt += 1

            print(ms, mt)
            if ms < mt:
                ms = mt
        print(used, g, i, cnt, ms)
        print(st)
        if 0 in used:
            g = used.index(0)
        else:
            break
