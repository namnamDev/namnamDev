import sys
from pprint import pprint

sys.stdin = open("ExpertAcademy5550.txt")

li = ["c", "r", "o", "a", "k"]
for tc in range(1, int(input()) + 1):
    st = input()
    used = [0] * len(st)
    g = 0
    cnt = 0
    maxs = 0
    while g < len(st) - 4:
        maxTemp = 1
        i = g
        temp = 0
        usedTemp = list(used)
        idxs = []
        if st[g] == "c":
            while i < len(st):
                if i != g and st[i] == "c":
                    maxTemp += 1

                if st[i] == li[temp] and used[i] == 0 and i not in idxs:
                    idxs += [i]
                    temp += 1
                i += 1

                if temp == 5:
                    temp = 0
                    cnt += 1
                    # print(idxs)
                    for g in idxs:
                        used[g] = 1
                    idxs = []
                    break
        if maxs < maxTemp:
            maxs = maxTemp

        if usedTemp == used:
            maxs = -1
            break
        # print(used, g, i, cnt, maxs)
        # print(st)
        if 0 in used:
            g = used.index(0)
        else:
            break
    if 0 in used:
        maxs = -1

    print("#{} {}".format(tc, maxs))
