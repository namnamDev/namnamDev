import sys

sys.stdin = open('Baekjoon1213.txt')


def cho(paArr):
    print(paArr)
    global an
    if an:
        return
    if len(paArr) == len(a):
        tempPa = list(paArr)
        for x in range(len(a) // 2):
            if tempPa[x] != tempPa[-x - 1]:
                return
        an = paArr
        return
    for ii in range(len(a)):
        t = paArr + a[ii]
        if not vi[ii] and not aa.get(t):
            vi[ii] = 1
            aa[t] = 1
            cho(t)
            vi[ii] = 0


a = list(input())
a.sort()
vi = [0] * len(a)
aa = {}
an = ""
for i in range(len(a)):
    vi[i] = 1
    cho(a[i])
    vi[i] = 0
if an:
    print(an)
else:
    print("I'm Sorry Hansoo")
