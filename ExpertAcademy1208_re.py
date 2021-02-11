import sys
sys.stdin = open("ExpertAcademy1208.txt")


for i in range(1, 11):
    d = int(input())
    a = list(map(int, input().split()))
    r = [0] * 100
    c = 0
    for g in a:
        r[g - 1] += 1
    for j in range(d):
        while r[0] == 0:
            r = r[1:]
        while r[-1] == 0:
            r = r[:-1]
        r[-1] -= 1
        r[-2] += 1
        r[0] -= 1
        r[1] += 1

    while r[0] == 0:
        r = r[1:]
    while r[-1] == 0:
        r = r[:-1]
    for f in r:
        c += 1
    print("#{} {}".format(i, c - 1))
